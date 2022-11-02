import os

import pytest
import tarfile
import zipfile

from solution import tar_to_zip
import re


@pytest.fixture
def test_tarfile(tmp_path):
    for index, letter in enumerate('abcde', 1):
        with open(tmp_path / f'{letter * index}.txt', 'w') as f:
            f.write(f'{letter * index}\n' * 100)

    tf = tmp_path / 'mytar.tar'
    with tarfile.open(tf, 'w') as t:
        for index, letter in enumerate('abcde', 1):
            t.add(tmp_path / f'{letter * index}.txt')

    return tf


@pytest.fixture
def test_textfile(tmp_path):
    tf = tmp_path / 'testfile.txt'
    with open(tf, 'w') as f:
        for i in range(10):
            f.write(f'Line {i}\n')

    return tf


def test_tar_to_zip(tmp_path, test_tarfile):
    tar_to_zip(test_tarfile, zippath=tmp_path)

    assert len(list(tmp_path.glob('*.zip'))) == 1

    zf = zipfile.ZipFile(tmp_path / 'mytar.zip')
    zf.extractall(path=tmp_path)
    assert len(list(tmp_path.glob('*.txt'))) == 5


def test_bad_file(tmp_path, test_textfile, capsys):
    tar_to_zip(test_textfile)

    captured_stdout, captured_stderr = capsys.readouterr()

    assert "Couldn't read from" in captured_stdout


# @pytest.mark.skip
def test_example(tmp_path):
    target_files = ('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')
    in_files = []
    os.chdir(tmp_path)
    txt_files = list(tmp_path / f"{n[:n.index('.')]}.txt" for n in target_files)
    for tf in txt_files:
        tf.write_text(f"content of {tf.name}")
    for i, f_name in enumerate(target_files):
        file_path = tmp_path / f_name
        mode = 'w:'
        if file_path.suffix in ('.gz', '.bz2'):
            mode += file_path.suffix[1:]
        with tarfile.open(file_path, mode) as tar:
            tar.add(txt_files[i].parts[-1])
        in_files.append(file_path)
        txt_files[i].unlink()

    tar_to_zip(*in_files, zippath=tmp_path)
    assert len(list(tmp_path.glob('*.zip'))) == len(target_files)

    for cur_zip in tmp_path.glob('*.zip'):
        zf_name = cur_zip.name
        base_name = zf_name.removesuffix('.zip')
        zf = zipfile.ZipFile(cur_zip)
        zf.extractall(path=tmp_path)
        with open(tmp_path / f"{base_name}.txt") as tf:
            content = tf.read()
            assert re.match(r'content of .*' + base_name, content)
