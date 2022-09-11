import os, sys
try:
    __import__("c").Main()
except Exception as e:
    exit(str(e))
