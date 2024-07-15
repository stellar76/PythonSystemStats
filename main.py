import os
import json
import time
import math
import psutil
from flask import Flask, json
from flask_cors import CORS

def get_Os():
    return {
        "kernal":  os.uname().release,
        "system": os.uname().sysname,
        "node": os.uname().nodename,
        "machine": os.uname().machine 
    }

def get_Cpu():
    return {
        "phys_cores": psutil.cpu_count(logical=False),
        "total_threads": psutil.cpu_count(logical=True),
        "proc_speed": psutil.cpu_freq().current,
        "proc_per_usage": dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
        "proc_avg_usage": psutil.cpu_percent(interval=1)
    }

def get_Mem():
    return {
        "total_mem": psutil.virtual_memory().total / (1024 ** 3),
        "avail_mem": psutil.virtual_memory().available / (1024 ** 3),
        "used_mem": psutil.virtual_memory().used / (1024 ** 3)
    }

def get_Net(): 
    netcounts = psutil.net_io_counters()
    return{
        "sent": netcounts.bytes_sent,
        "received" :netcounts.bytes_recv 
    }

def get_Up():
    current = time.time()
    boot = psutil.boot_time()
    uptime = current - boot
    seconds = uptime // 60
    minutes = seconds // 60
    hours =  minutes // 60
    days = hours // 24
    return{
        "boot": boot,
        "current": current,
        "uptime": uptime,
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days
    }



stats = Flask(__name__)
cors = CORS(stats, resources={r"/stats/*": {"origins": "*"}})

@stats.route('/stats', methods=['GET'])
def get_Stats():
    return json.dumps({
        "os": get_Os(),
        "cpu": get_Cpu(),
        "mem": get_Mem(),
        "net": get_Net(),
        "uptime": get_Up()
    })

if __name__ == '__main__':
    stats.run()