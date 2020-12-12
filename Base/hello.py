import os
import platform
import psutil


print ("Hello...")
print os.name


print platform.platform()
print platform.system()
print platform.release()
print platform.version()


psutil.disk_partitions()

