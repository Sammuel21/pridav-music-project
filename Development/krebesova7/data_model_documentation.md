# Spotify Track Data Documentation

## Data Fields

### Track Info
1. id (string)
   - Spotify's unique identifier for the track

2. name (string)
   - The name/title of the track

3. track_number (integer)
   - The track's position in its disc/album

4. disc_number (integer)
   - The disc number for albums with multiple discs

5. duration_ms (integer)
   - Track duration in milliseconds

6. popularity (integer)
   - Spotify's popularity score (0-100)
   - Higher numbers indicate more popular tracks

7. explicit (boolean)
   - Whether the track contains explicit content

8. artists (string)
   - Comma-separated list of all artists performing the track

9. artist_ids (string)
   - Comma-separated list of Spotify IDs for all artists performing the track

### Album Info
10. album (string)
    - Name of the album containing the track

11. album_total_tracks (integer)
    - Total number of tracks in the album

12. album_artists (string)
    - Comma-separated list of all artists credited on the album

13. album_artist_ids (string)
    - Comma-separated list of Spotify IDs for all album artists

14. album_release_date (string)
    - Release date of the album in YYYY-MM-DD format

### Availability Info
15. restrictions (object, nullable)
    - Any restrictions applied to the track
    - Null if no restrictions exist

16. available_markets (array, nullable)
    - List of country codes where the track is available
    - Null if available everywhere
