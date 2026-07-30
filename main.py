import json
from pathlib import Path

year = input("year to analyze: ")
FILE_PATH = f"Streaming_History_Audio_{year}.json"


if not(Path(FILE_PATH).exists()):
    print("file path invalid")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

total_entries = len(data)

def analyze(metadata, label):
    counts = {}

    for record in data:
        item = record.get(metadata)
        if item:
            counts[item] = counts.get(item, 0) + 1

    item_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    print(f"You listened to {len(item_sorted)} {label}\n")

    for i in range(len(item_sorted) - 1):
        name, count = item_sorted[i]
        _, next_count = item_sorted[i+1]
        ratio = (count / next_count)
        percentage = (count / total_entries) * 100

        print(f"{count:>5} | {ratio:>6.3f}x | {percentage:>6.3f}% | {name}")

    if item_sorted:
        last_name, last_count = item_sorted[-1]
        last_percentage = (last_count / total_entries) * 100

        print(f"{last_count:>5} | last    | {last_percentage:>7.4f}% | {last_name}")


choice = input("song or artist: ")
print(f"You have {total_entries} total entries")
if choice == "song":
    analyze("master_metadata_track_name", "songs")
elif choice == "artist":
    analyze("master_metadata_album_artist_name", "artists")
else:
    print("select song or artist")
