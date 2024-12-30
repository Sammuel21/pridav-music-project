# ETLs & Transformation pipeline

import os
import sys

sys.dont_write_bytecode = True

import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures

from sklearn.impute import SimpleImputer, KNNImputer

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# ---------

class ETL(BaseEstimator, TransformerMixin):
    '''Custom ETL model, abstract class, when creating an ETL use class inheritance and overwrite
       self.transform method with custom transformation, must return transformed X.'''

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return X



class FrequencyEncoder(ETL):

    TARGET_COL = 'artist_name'

    def __init__(self):
        self.frequencies = None
        self.default_value = 0

    
    def fit(self, X, y=None):
        freqs = X[self.TARGET_COL].str.split(',').explode().value_counts()
        self.frequencies = freqs.to_dict()
        return self
    

    def transform(self, X, y=None):

        X_new = X.copy()

        X_new[self.TARGET_COL] = X[self.TARGET_COL].map(self.frequencies).fillna(self.default_value)

        return X_new



class CircleOfFifthsEncoding(ETL):

    TARGET_COLUMN = 'key'

    # Pôvodný mapping z datasetu (chromatic scale: 0–11)
    # Tento mapping je založený na poltónových intervaloch.
    chromatic_scale = {
        0: "C",
        1: "C#/Db",
        2: "D",
        3: "D#/Eb",
        4: "E",
        5: "F",
        6: "F#/Gb",
        7: "G",
        8: "G#/Ab",
        9: "A",
        10: "A#/Bb",
        11: "B"
    }

    # Korektný ordinal pre Circle of Fifths:
    # Táto sekvencia reflektuje harmonické vzťahy medzi kľúčmi:
    # každý nasledujúci kľúč je vzdialený o kvintu (7 poltónov).
    circle_of_fifths_mapping = {
        0: 0,  # C
        7: 1,  # G
        2: 2,  # D
        9: 3,  # A
        4: 4,  # E
        11: 5, # B
        6: 6,  # F#/Gb
        1: 7,  # C#/Db
        8: 8,  # G#/Ab
        3: 9,  # D#/Eb
        10: 10, # A#/Bb
        5: 11  # F
    }


    def transform(self, X, y=None):

        X_new = X.copy()

        ordinal_remapping = X[self.TARGET_COLUMN].map(self.circle_of_fifths_mapping)

        theta = (2 * np.pi / 12) * ordinal_remapping

        x = np.cos(theta)
        y = np.sin(theta)

        X_new = X_new.drop(self.TARGET_COLUMN, axis=1, errors='ignore')

        X_new['key_x'] = x
        X_new['key_y'] = y

        return X_new



class ConvertNull(ETL):
    
    def __init__(self, columns=None, input_value=-1, output_value=np.nan):

        if columns is None:
            self.columns = []
        else:
            self.columns = columns

        self.input_value = input_value
        self.output_value = output_value

    
    def transform(self, X):
        X_new = X.copy()
        X_new[self.columns] = X_new[self.columns].replace(self.input_value, self.output_value)
        return X_new




# --------- Pipelines

numeric_pipeline = Pipeline(steps=[
    ('scaling', StandardScaler())
])


artist_name_pipeline = Pipeline(steps=[
    ('encoding', FrequencyEncoder()),
    ('scaling', StandardScaler())
])


transformations = ColumnTransformer(transformers=[
    
    ('onehot_encoding', OneHotEncoder(sparse_output=False), []),
    ('trigonometric_encoding', CircleOfFifthsEncoding(), []),
    ('artist_encoding', artist_name_pipeline, []),
    ('nummeric_processing', numeric_pipeline, [])

], remainder='drop')


preprocessing = Pipeline(steps=[
    ('null_values', ConvertNull(columns=[])),
    ('transformation', transformations)
])

