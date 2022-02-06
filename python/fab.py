from ctypes import CDLL, c_char_p, c_float, c_int
from os import path
from sys import platform


if platform == "win32":
    lib_name = "fab.dll"
elif platform == "darwin":
    lib_name = "libfab.dylib"
elif platform.startswith("linux") or platform == "linux":
    lib_name = "libfab.so"

_libfab = CDLL(path.join(path.dirname(__file__), lib_name))

def say_hello(name):
    return _libfab.say_hello(name.encode())
_libfab.say_hello.argtypes = [c_char_p]
_libfab.say_hello.restype = None


def add(a, b):
    return _libfab.add(a, b)
_libfab.add.argtypes = [c_int, c_int]
_libfab.add.restype = c_int


def approach(t, target, delta):
    return _libfab.approach(t, target, delta)
_libfab.approach.argtypes = [c_float, c_float, c_float]
_libfab.approach.restype = c_float
