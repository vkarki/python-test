#!/usr/bin/python3
import prometheus_client
import time
import psutil
import os
import subprocess
import func

UPDATE_PERIOD = 15 
CUSTOM_SYSTEM_USAGE = prometheus_client.Gauge('system_usage','Hold current system resource usage',['resource_type'])
CUSTOM_SYSTEM_STATS = prometheus_client.Gauge('service_health', 'Health of the system',['service_name','host_name'] )
CUSTOM_SYSTEM_ZOMBIE = prometheus_client.Gauge('zombie_process','zombie process running in the system',['host_name'])
CUSTOM_SYSTEM_OPEN_FILES = prometheus_client.Gauge('open_files','openfiles of an application',['host_name'])
service = 'main.py'
host = os.uname()[1]

if __name__ == '__main__':
  prometheus_client.start_http_server(9817)  
while True:
  CUSTOM_SYSTEM_USAGE.labels('CPU').set(psutil.cpu_percent())
  CUSTOM_SYSTEM_USAGE.labels('Memory').set(psutil.virtual_memory()[2])
  CUSTOM_SYSTEM_STATS.labels(service,host).set(func.service_status(service))
  CUSTOM_SYSTEM_ZOMBIE.labels(host).set(func.zombie_count())
  CUSTOM_SYSTEM_OPEN_FILES.labels(host).set(func.open_files(service))
  time.sleep(UPDATE_PERIOD)
