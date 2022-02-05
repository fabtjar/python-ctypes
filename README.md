## Python Ctypes
A small test to get Python to use compiled C code with ctypes.

### Building
Compile the C code:
```bash
cd fab/
cmake -S . -B build/
cd build/
make
```
Use the compiled C code with Python:
```bash
cd ../../python/
python3 main.py
```
