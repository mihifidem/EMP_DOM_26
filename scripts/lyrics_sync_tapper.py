#!/usr/bin/env python3
"""Terminal tool to create lyrics_sync.json files by tapping time markers.

Usage example:
    python scripts/lyrics_sync_tapper.py --lyrics-file letra.txt --output lyrics_sync.json

Workflow:
1. Start your song in any player.
2. In this tool, press Enter when each lyric line starts.
3. The script exports JSON with objects: {"time": <seconds>, "text": <line>}.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a synced lyrics JSON file by tapping Enter for each line."
    )
    parser.add_argument(
        "--lyrics-file",
        required=True,
        type=Path,
        help="Path to a UTF-8 text file with one lyric line per row.",
    )
    parser.add_argument(
        "--output",
        default="lyrics_sync.json",
        type=Path,
        help="Output JSON path (default: lyrics_sync.json).",
    )
    parser.add_argument(
        "--offset",
        default=0.0,
        type=float,
        help="Seconds to add to each captured time (default: 0.0).",
    )
    parser.add_argument(
        "--precision",
        default=2,
        type=int,
        help="Decimal places for time values (default: 2).",
    )
    return parser.parse_args()


def load_lyrics(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Lyrics file not found: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()
    lyrics = [line.strip() for line in lines if line.strip()]

    if not lyrics:
        raise ValueError("Lyrics file is empty after removing blank lines.")

    return lyrics


def tap_times(lyrics: list[str], offset: float, precision: int) -> list[dict[str, float | str]]:
    print("\nReady to sync.")
    print("Instructions:")
    print("- Press Enter at the exact moment each line starts.")
    print("- Type 'b' then Enter to go back one line.")
    print("- Type 'q' then Enter to finish and export current progress.\n")

    input("Press Enter to start timer (start your song at the same time)...")
    start = time.perf_counter()

    captured: list[dict[str, float | str]] = []
    index = 0

    while index < len(lyrics):
        line = lyrics[index]
        command = input(f"[{index + 1}/{len(lyrics)}] {line}\n> ").strip().lower()

        if command == "q":
            print("Stopping early and exporting captured lines.")
            break

        if command == "b":
            if captured:
                removed = captured.pop()
                index -= 1
                print(f"Removed line {index + 1}: {removed['text']}")
            else:
                print("Nothing to undo yet.")
            continue

        now = time.perf_counter()
        timestamp = round((now - start) + offset, precision)
        captured.append({"time": timestamp, "text": line})
        index += 1

    return captured


def save_output(path: Path, data: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    args = parse_args()
    lyrics = load_lyrics(args.lyrics_file)
    synced = tap_times(lyrics, args.offset, args.precision)
    save_output(args.output, synced)

    print(f"\nDone. Exported {len(synced)} lines to: {args.output}")


if __name__ == "__main__":
    main()
