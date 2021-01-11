#!/usr/bin/python3
import yaml
import os 

fname = "test.yml"

if os.path.exists(fname):
    with open(fname) as f:
        dct = yaml.safe_load(f)
    print(dct)
    ip = ["192.168.1.1:9100","192.168.1.2:9100","192.168.1.3:9100"]
    for i in ip:
        dct[0]["targets"].append(i)
    with open(fname,'w') as f:
        yaml.dump(dct,f)

else:
    dct = [{"targets":["192.168.1.4:9100"]}]
    with open(fname, "w") as f:
        yaml.dump(dct,f)
