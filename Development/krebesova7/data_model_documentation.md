# Spotify Track Data Documentation

## Data Sources

The dataset consists of two main CSV files:
1. `spotify_tracks_kaggle_weekly.csv` - Contains track information and audio features (sourced from kaggle)
2. `spotify_tracks_artist_details.csv` - Contains detailed artist information for each track (sourced from Spotify API)

## Data Fields

### Track Info (spotify_tracks_kaggle_weekly.csv)
1. track_id (string)
   - Spotify's unique identifier for the track

2. track_name (string)
   - The name/title of the track

3. artist_name (string)
   - Name(s) of the artist(s) performing the track

4. year (integer)
   - Release year of the track

5. popularity (integer)
   - Spotify's popularity score (0-100)
   - Higher numbers indicate more popular tracks

6. artwork_url (string)
   - URL to the album/track artwork image

7. album_name (string)
   - Name of the album containing the track

8. acousticness (float)
   - Confidence measure of whether the track is acoustic (0.0 to 1.0)

9. danceability (float)
   - How suitable a track is for dancing based on musical elements (0.0 to 1.0)

10. duration_ms (integer)
    - Track duration in milliseconds

11. energy (float)
    - Perceptual measure of intensity and activity (0.0 to 1.0)

12. instrumentalness (float)
    - Predicts whether a track contains no vocals (0.0 to 1.0)

13. key (integer)
    - The key the track is in. Integers map to pitches using standard Pitch Class notation

14. liveness (float)
    - Detects presence of an audience in the recording (0.0 to 1.0)

15. loudness (float)
    - Overall loudness in decibels (dB)

16. mode (integer)
    - Modality of the track (0 = minor, 1 = major)

17. speechiness (float)
    - Presence of spoken words in the track (0.0 to 1.0)

18. tempo (float)
    - Overall estimated tempo in beats per minute (BPM)

19. time_signature (integer)
    - Estimated time signature of the track

20. valence (float)
    - Musical positiveness conveyed by the track (0.0 to 1.0)

21. track_url (string)
    - URL to the track on Spotify

22. language (string)
    - Language of the track lyrics

### Artist Details (spotify_tracks_artist_details.csv)
1. track_id (string)
   - Foreign key linking to the tracks dataset

2. track_name (string)
   - Name of the track (duplicate from tracks dataset)

3. artist_count (integer)
   - Number of artists featured on the track

4. artist_ids (string)
   - Comma-separated list of Spotify IDs for all artists

5. artist_names (string)
   - Comma-separated list of artist names

6. artist_popularities (string)
   - Comma-separated list of popularity scores for each artist

7. artist_genres (string)
   - Pipe-separated list of comma-separated genre lists for each artist

8. artist_followers (string)
   - Comma-separated list of follower counts for each artist

9. avg_artist_popularity (float)
   - Average popularity score across all artists on the track
