"""MP4 files info.

Takes a directory name, as a command-line argument, and does the following with it:
- finds all the *.mp4 files in that directory
- calculates the duration, in minutes, of each video
- creates a NumPy-array/Pandas-series from these durations
- displays statistics for these durations, in minutes for: min, max, mean, and std
- displays the total time, in hh:mm format, of the videos
"""
import sys
import glob
import pandas as pd
from datetime import time
from tinytag import TinyTag


def get_mp4_files(path: str) -> list:
    """Return paths to MP4 files in given directory.

    :param path: path to directory with MP4 files
    :return: list of MP4 files paths
    """
    return glob.glob(f'{path}/*.mp4')


def get_mp4_file_duration(file_path: str) -> float:
    """Retrieve MP4 file duration in minutes.

    :param file_path: path to the MP4 file
    :return: duration in minutes
    """
    tag = TinyTag.get(file_path)
    return tag.duration / 60


def minutes_to_hhmm_time(minutes: float) -> str:
    """Return hh:mm formatted string for given duration.

    :param minutes: duration in minutes
    :return: hh:mm formatted duration
    """
    hour, minute = int(minutes // 60), int(minutes % 60)
    this_time = time(hour=hour, minute=minute)
    return f"{this_time:%H:%M}"


def display_videos_stat(videos: pd.Series):
    """Given a videos duration Series, print its statistics to console.

    :param videos: Series of videos duration
    :return: None
    """
    total_minutes = videos.sum()
    print(f"Total time: {minutes_to_hhmm_time(total_minutes)}")
    print(f"Number of files: {len(videos)}")
    print(f"min: {videos.min():.2f} minutes, max: {videos.max():.2f} minutes, "
          f"mean: {videos.mean():.2f} minutes, std: {videos.std():.2f} minutes.")
    # print(videos)


def main():
    directory = sys.argv[1]
    files = get_mp4_files(directory)
    videos = pd.Series({f: get_mp4_file_duration(f) for f in files})
    display_videos_stat(videos)


if __name__ == '__main__':
    main()
