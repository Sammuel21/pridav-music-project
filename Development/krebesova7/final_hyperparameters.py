import joblib
import os
from pprint import pformat
from contextlib import redirect_stdout
import io

def load_and_print_hyperparameters():
    output = io.StringIO()
    with redirect_stdout(output):
        print("Best Hyperparameters for Each Model:\n")
        
        print("Linear Models:")
        print("-" * 50)
        
        lr_path = os.path.join('..', '..', 'Prod', 'Models', 'Linear', 'linear-optimized-lr.joblib')
        if os.path.exists(lr_path):
            lr_model = joblib.load(lr_path)
            print("\nLinear Regression:")
            print(pformat(lr_model.get_params()))
        
        ridge_path = os.path.join('..', '..', 'Prod', 'Models', 'Linear', 'linear-optimized-ridge.joblib')
        if os.path.exists(ridge_path):
            ridge_model = joblib.load(ridge_path)
            print("\nRidge Regression:")
            print(pformat(ridge_model.get_params()))
        
        lasso_path = os.path.join('..', '..', 'Prod', 'Models', 'Linear', 'linear-optimized-lasso.joblib')
        if os.path.exists(lasso_path):
            lasso_model = joblib.load(lasso_path)
            print("\nLasso Regression:")
            print(pformat(lasso_model.get_params()))
        
        print("\nEnsemble Models:")
        print("-" * 50)
        
        xgb_path = os.path.join('..', '..', 'Prod', 'Models', 'Ensemble', 'xgboost-regressor-optimized-30-columns.joblib')
        if os.path.exists(xgb_path):
            xgb_model = joblib.load(xgb_path)
            print("\nXGBoost Regressor:")
            print(pformat(xgb_model.get_params()))
    
    with open('model_hyperparameters.txt', 'w') as f:
        f.write(output.getvalue())

if __name__ == '__main__':
    load_and_print_hyperparameters()
