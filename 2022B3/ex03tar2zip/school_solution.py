#!/usr/bin/env python3

import tarfile
import os.path
import pathlib
from zipfile import ZipFile, ZIP_DEFLATED


def tar_to_zip(*filenames, zippath=None):
    if not zippath:
        zippath = pathlib.Path('.')

    for one_tarfile in filenames:
        try:
            with ZipFile(zippath / 'output.zip', 'w',
                         compression=ZIP_DEFLATED) as zf:
                tf = tarfile.open(one_tarfile, 'r')
                for one_tarinfo in tf:
                    tf.extract(one_tarinfo, path='/tmp/')
                    zf.write(f'/tmp/{one_tarinfo.name}',
                             arcname=one_tarinfo.name)
        except tarfile.TarError as e:
            print(f"Couldn't read from '{one_tarfile}'; ignoring")


if __name__ == '__main__':

    tar_to_zip('passwd',
               '/Users/reuven/Downloads/decorator-4.2.0.tar.gz',
               '/Users/reuven/Downloads/sample.tgz',
               '/Users/reuven/Downloads/textfiles.tar')
