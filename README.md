# spotify-data-analysis
Simple Python script that analyzes your Spotify listening history.

## Prerequisites
Python 3.14

## Usage
1. Download <a href="main.py" download>main.py</a>.
2. Request your Spotify extended listening history from https://www.spotify.com/account/privacy/.
   - Or use the provided <a href="Streaming_History_Audio_6767.json" download>test file</a>.
3. Once the extended listening history file is available, download and extract it.
   - Skip this step if you're using the test file.
4. Put `main.py` in the same folder as the json files.
5. Enter the year when prompted. (example: 2026)
6. Enter either 'artist' or 'song' when prompted.

## Output reading guide
Times streamed | Times more streamed than next entry | Percentage | Name (song/artist)

### Example
7979 |  1.423x | 49.338% | ZUTOMAYO\
5608 | 13.481x | 34.677% | Eve

ZUTOMAYO is:
- streamed 7979 times
- streamed 1.423 times more than next entry (Eve)
- makes up 49.338% out of all streams in that year

Eve is:
- streamed 5608 times
- streamed 13.481 times more than next entry
- makes up 34.677% out of all streams in that year
