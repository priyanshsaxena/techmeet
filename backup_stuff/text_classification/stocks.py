import urllib,time,datetime,csv
import matplotlib.pyplot as plt

def getPrices(string_symbol):
  num_days = 2
  url_string = "http://chartapi.finance.yahoo.com/instrument/1.0/{0}/chartdata;type=quote;range={1}d/csv".format(string_symbol,num_days)
  csv = urllib.urlopen(url_string).readlines()
  # csv.reverse()
  x = []

  for bar in xrange(0,len(csv)-1):
    if(csv[bar].split(",")[0].isdigit()):
      csv_tmp,_ = csv[bar].split("\n")
      item = map(float,csv_tmp.split(","))
      _timestamp = datetime.datetime.fromtimestamp(item[0]) - datetime.timedelta(minutes=570) # Converting IST to EDT
      time = datetime.datetime.now() - datetime.timedelta(hours=9,minutes=30) #US time
      
      if(_timestamp.day == time.day):
        break
      # print _timestamp
      _timestamp = str(_timestamp.hour)+":"+str(_timestamp.minute)+":"+str(_timestamp.second)
      _close,_high,_low,_open,_volume = item[1:]
      x.append([_timestamp,item[0],_close,_high,_low,_open,_volume])
      
  return x
 
if __name__ == '__main__':
  q = getPrices("jpm") # Stock ticker symbol, num_days
  with open("output.csv", "wb") as f:
      writer = csv.writer(f)
      writer.writerows(q)