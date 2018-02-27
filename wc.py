
import os
import time
a=0
b=1
while a<10:
   cmd= "fswebcam -F 3 --fps 20 -r 1200x800 /home/user/Desktop/abc"+str(b)+".jpg"
   os.system(cmd)
   time.sleep(1)
   print("pic Taken")
   a=a+1
   b=b+1
    

