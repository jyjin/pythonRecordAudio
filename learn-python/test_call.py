import sys
import os

lib_path = os.path.abspath(os.path.join('./util'))
print(lib_path)
sys.path.append(lib_path)

import time_count
time_count.count(10)