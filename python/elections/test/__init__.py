import sys
print(sys.version_info[0])
raise Exception
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")
