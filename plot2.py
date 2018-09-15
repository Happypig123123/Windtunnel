import matplotlib
matplotlib.use('Agg')
#DO NOT CHANGE FIRST 2 LINES ORDER AND CONTENT!!!!
import boto3
from urllib.request import urlretrieve
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import math
#define s3 url
print("Downloading Spreadsheet")
url = 'https://s3-ap-southeast-2.amazonaws.com/windtunnelgraph/File.xlsx'
# save url locally
urlretrieve(url, 'File.xlsx')
#carry on
df = pd.read_excel('File.xlsx', sheetname='Sheet1',header=None)
print("Fetched File from S3.")
print("Calculating plot Points...")
length = int(df.shape[0])
#print("Amount of RowS:")
#print(df.shape[0])
# lets find the drag values and add to an array
drag = [0,0,0,0,0,0,0]
for i in range(7, length):
    temp = (df[16][i])-(df[6][i])
    if isinstance(temp, int) == 1:
    	drag.append((temp/11.64*0.1))
        #print(temp, df[16][i], df[6][i])
# lets find the average wind values
flow = [0,0,0,0,0,0,0]
b = 9999
for i in range(7, length):
    temp = ((df[17][i])+(df[7][i]))/2
    #print((df[17][i]),(df[7][i]))
    if math.isnan(temp) == 0:

    	if temp != b:
    		flow.append((temp*10/36))
    	else:
    		flow.append(flow[i-1]+0.05)
    b = temp

#for i in range(7, len(drag)):
	#print(drag[i], ",",flow[i])
#Create Data Average
x = []
y = []
for i in range(1, len(drag)):
    if i % 5 == 0:
        x.append(flow[i])
        y.append(drag[i])
#add some titles:
plt.ylabel('Drag (N)')
plt.xlabel('Wind Speed (M/S) (Max speed = 11m/s)')
plt.title('Drag compared to Wind Speed')

#PLOT Nothing
#plt.plot([0,2,4,6,8,10,11,11],[0,0,0,0,0,0,0,0])

#Plotting to our canvas
#lt.plot(flow,drag, label='Average Drag',color="magenta") #DONT WANT THIS! AS NOT TRUE AVERAGE DRAG
#(FLOW,DRAG)
#Setting X axis values




#Showing what we
plt.savefig('simple.png')

# SAVE COMPLEX VERSION
plt.plot(flow,drag,label='Drag',color="orange")
#(FLOW,DRAG)
#Showing what we
plt.legend()
plt.savefig('plot1.png')
print("Plotting Done.")

#Lets upload the file to S3 so the user can download it using the graphics interface
print("Uploading.....")
# Let's use Amazon S3
s3 = boto3.resource('s3')
# Save Plot 1 to bucket.
data = open('plot1.png', 'rb')
s3.Object('windtunnelgraph', 'plot1.png').delete()
s3.Bucket('windtunnelgraph').put_object(Key='plot1.png', Body=data)
s3.Object('windtunnelgraph', 'File.xlsx').delete() #UNCOMENT UNLESS DEVELOPING
#Program.exit()
print("Succesfully uploaded content to S3 Bucked, windtunnelgraph.")
