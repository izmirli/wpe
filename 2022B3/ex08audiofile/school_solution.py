#!/usr/bin/env python3

import tinytag
import glob
import datetime
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("You need to provide a directory name! ")
    sys.exit()

dirname = sys.argv[1].rstrip('/')
print(f"Looking at '{dirname}'")
timings = []

for one_filename in glob.glob(f'{dirname}/*.mp4'):
    t = tinytag.TinyTag.get(one_filename)
    timings.append(t.duration / 60)

s = pd.Series(timings)
print(s.describe())
print(f"Total time is: {datetime.timedelta(minutes=s.sum())}")
