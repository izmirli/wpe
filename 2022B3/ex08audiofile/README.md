# WPE 2022 B3 Exercise 8: Audiofile

Write a Python program that takes a directory name as a command-line argument, and does the following with it:
- finds all of the *.mp4 files in that directory
- calculates the duration, in minutes, of each video
- creates a NumPy array or (my preference) a Pandas series from these durations
- displays the descriptive statistics for these durations, in minutes -- at the very least, min, max, mean, and std
- displays the total time, in hh:mm format, of the videos

School solution used the following packages:
- sys
- glob
- datetime
- pandas
- tinytag (from PyPI)
