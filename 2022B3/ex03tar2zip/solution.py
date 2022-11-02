"""Tar to zip.

Take one or more filenames, each of which is assumed to be a tarfile
(with or without compression). For each filename, the function will
create a new zipfile with the same contents, but (obviously) in ".zip"
format rather than in ".tar.gz" format.
"""
import os
import tarfile
import tempfile
import zipfile


def tar_to_zip(*files, zippath=None):
    """Convert given tar file to zip format.

    If a file cannot be untar'ed for whatever reason, print an error,
    but continue.

    :param files: all positional arguments as tar file names
    :param zippath: an optional path (as str or some path object) for zip files
    :return: None
    """
    working_dir = os.getcwd()
    zip_dir = zippath if zippath is not None else working_dir
    tmp_dir = tempfile.TemporaryDirectory()

    for cur_file in files:
        os.chdir(working_dir)
        if not tarfile.is_tarfile(cur_file):
            print(f"Couldn't read from {cur_file}")
            continue
        base_name = str(cur_file)
        base_name = base_name[:base_name.index('.tar')]
        tar_file = tarfile.open(cur_file)

        os.chdir(zip_dir)
        zip_file = zipfile.ZipFile(f"{base_name}.zip", mode='w')

        os.chdir(tmp_dir.name)
        for tared in tar_file:
            tar_file.extract(tared)
            zip_file.write(tared.name)

        zip_file.close()

    os.chdir(working_dir)
    tmp_dir.cleanup()
