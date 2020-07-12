#!/usr/bin/env python3
#above shebang line is used to run the script by only file name, as it set the path, but before running permisson is required e.g chmod -x file.py
import shutil #module to check disk info
import psutil #module to check cpu info
def check_disk_usage(disk):
    """This function return True, if % availabe disk space is greater than 20."""
    du=shutil.disk_usage(disk)
    perc_free_space_available=du.free/du.total*100
    return perc_free_space_available > 20
def check_cpu_usage():
    """This function return True, if % cpu use is less than 75."""
    usage=psutil.cpu_percent(1)
    return usage < 75
if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!")
else:
    print("Everything is OK!")
