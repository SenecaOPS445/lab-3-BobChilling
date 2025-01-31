#!/usr/bin/env python3
# Author ID: [wcao23]

import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/'$ | awk '{print $4}'",
                            shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()
print(free_space())


