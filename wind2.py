import boto3
import os
from boto3 import client
s3 = boto3.resource('s3')
bucket = s3.Bucket('windtunnelgraph')
key = 'File.xlsx'
#Delete this line unless excecuting script not from script directory:
os.chdir('/home/ubuntu/wind/program') #Write the directory of *THIS SCRIPT's* folder here.


while 1 == 1:
    objs = list(bucket.objects.filter(Prefix=key))
    while not(len(objs) > 0 and objs[0].key == key): #wait for new file to be uploaded.
        objs = list(bucket.objects.filter(Prefix=key))
        #Check for Excel doc:

    print("New File Uploaded")
    s3.Object('windtunnelgraph', 'plot1.png').delete()
    os.system("python3 plot2.py") #Plot new file
