import pandas as pd
import datetime

data=pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\Car.csv')
ldata=data.to_numpy()
lendata=len(ldata)
nowtime=datetime.datetime.now().date()
new_indcies=pd.date_range(nowtime,periods=lendata,freq=pd.offsets.DateOffset(years=1))

data.index=new_indcies

subdata=data.truncate(before='2028',after='2035')
print(subdata)
