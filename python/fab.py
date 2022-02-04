import ctypes
from sys import platform


if platform == 'win32':
    lib_name = "libfab.dll"
elif platform == 'darwin':
    lib_name = "libfab.dylib"
elif platform.startswith('linux') or platform == 'linux':
    lib_name = "libfab.so"


_libfab = ctypes.CDLL(f"../fab/build/{lib_name}")


def say_hello(name):
    return _libfab.say_hello(name.encode())
_libfab.say_hello.argtypes = [ctypes.c_char_p]
_libfab.say_hello.restype = None


def add(a, b):
    return _libfab.add(a, b)
_libfab.add.argtypes = [ctypes.c_int, ctypes.c_int]
_libfab.add.restype = ctypes.c_int


def approach(t, target, delta):
    return _libfab.approach(t, target, delta)
_libfab.approach.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
_libfab.approach.restype = ctypes.c_float
