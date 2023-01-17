"""The end."""
from os import unlink


class TempFile:
    """Temporary file object, that on no more references to it, file is erased from disk."""

    def __init__(self, file, *args, **kwargs):
        self.file_path = file
        self.file_object = open(file, *args, **kwargs)

    def __del__(self):
        print('__del__ -> unlink')
        unlink(self.file_path)

    def __enter__(self):
        print('__enter__')
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ -> close')
        self.file_object.close()
        print('__exit__ -> after close')

    def __getattr__(self, item):
        return self.file_object.__getattribute__(item)
