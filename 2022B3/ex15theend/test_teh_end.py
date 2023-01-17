import pytest
import platform
from solution import TempFile
from os.path import isfile, exists


def test_simple(tmp_path):
    filename = tmp_path / 'myfile.txt'
    assert not exists(filename)
    f = TempFile(filename, 'w')
    f.write('abc\n')
    f.close()
    assert exists(filename)
    del f
    assert not exists(filename)


def test_methods(tmp_path):
    filename = tmp_path / 'myfile.txt'
    assert not exists(filename)
    f = TempFile(filename, 'w+')
    for one_word in 'abc def ghi jkl'.split():
        f.write(f'{one_word}\n')

    assert f.tell() == 20 if platform.system() == 'Windows' else 16
    f.seek(3)
    assert f.read(4) == '\ndef'

    f.close()
    assert exists(filename)
    del f
    assert not exists(filename)


def test_in_with(tmp_path):
    filename = tmp_path / 'myfile.txt'
    assert not exists(filename)
    outer_f = None
    with TempFile(filename, 'w') as f:
        f.write('abc\n')
        outer_f = f

    print(f"[t0]\n  f: {f};\n  outer_f: {outer_f}")
    assert exists(filename)
    del f
    print(f"del(f)")
    del outer_f
    print(f"del(outer_f)")
    assert not exists(filename)


def test_additional_reference(tmp_path):
    filename = tmp_path / 'myfile.txt'
    assert not exists(filename)
    with TempFile(filename, 'w') as f:
        f.write('abc\n')

    f2 = f
    assert exists(filename)
    del f
    assert exists(filename)
    del f2
    assert not exists(filename)
