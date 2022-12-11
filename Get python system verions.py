import sys
print ("Python version")
print (sys.version)
print ('Version info')
print (sys.version_info)

# Using platform module:
print ('Using platform module')
import platform
print (platform.python_version)

# Python version as tuple (major, minor, patchlevel) of strings:

print ('Python version as tuple (major, minor, patchlevel) of strings:')
import platform
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
