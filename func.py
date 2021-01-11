#!/usr/bin/python3

import prometheus_client
import time
import psutil
import os
import subprocess

def service_status(service):
    host = os.uname()[1]
    try:
        proc1 = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', service], stdin=proc1.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc3 = subprocess.Popen(['wc', '-l'], stdin=proc2.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
        proc2.stdout.close() # Allow proc2 to receive a SIGPIPE if proc3 exits.

        out, err = proc3.communicate()

        if err:
            status=0
        else:
            p=int(out)
            if p > 1:
                status=1
            else:
                status=0
    except:
        status=0
        return status
    return status

def zombie_count():
    try:
        proc1 = subprocess.Popen(['ps','-aux'],stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', 'Z'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc3 = subprocess.Popen(['sed', '1d'], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc4 = subprocess.Popen(['wc','-l'], stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        proc2.stdout.close()
        proc3.stdout.close()
        out,err = proc4.communicate()
    
        if err:
            count = 0
        else:
            if int(out) > 0:
                count = int(out) - 1
            else:
                count = int(out)
    except:
        count = 0
        return count
    return count

def get_pid(process_name):
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return proc.pid
        
def open_files(process_name):
    try:
        pid = str(get_pid(process_name))
        proc1 = subprocess.Popen(['sudo','lsof','-p', pid],stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['wc','-l'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out,err = proc2.communicate()

        if err:
            count = 0
        else:
            count = int(out) - 1
    
    except:
        count=0
        return count
        
    return count


