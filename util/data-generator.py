import os
import time
import requests
for root, dirs, files in os.walk('/Users/yishuanglu/Downloads/2017-03-08'):
     for file in files:
        with open(os.path.join(root, file), "r") as f:
            for line in f:
                r = requests.post("http://localhost:3000", json=line)
                time.sleep(1)  # delays for 1 seconds
                print r
