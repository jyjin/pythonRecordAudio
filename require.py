import sys
import os

def require(_path):
    lib_path = os.path.abspath(os.path.join(_path))
    print(lib_path)
    sys.path.append(lib_path)
    arr = _path.split('/')
    module_name = arr[len(arr)-1]
    print(arr)
    print(module_name) 
    print(type(module_name))
    # import '%s' % module_name


