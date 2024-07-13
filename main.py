import os
import json
import time
import psutil

def getOs():
    return {
        "kernal":  os.uname().release,
        "system": os.uname().sysname,
        "node": os.uname().nodename,
        "machine": os.unmam().machine 
    }

def getCpu():
    return {
        "phys_cores": psutil.cpu_count(logical=False),
        "total_threads": psutil.cpu_count(logical=True),
        "proc_speed": psutil.cpu_freq().current,
        "proc_per_usage": dict(enumarate(psutil.cpu_percent(percpu=True, interval=1))),
        "proc_avg_usage": psutil.cpu_percent(interval=1)
    }

def getMem():
    return {
        "total_mem": psutil.virtual_memory().total / (1024 ** 3),
        "avail_mem": psutil.virtual_memory().available / (1024 ** 3),
        "used_mem": psutil.virtual_memory().used / (1024 ** 3)
    }

