import csv

info={}
with open('./displacementByMonth.csv','r')as f:
  data = csv.reader(f)
  for row in data:
      location=row[1].split('_')[1]
      try:
          lastInfo=info[location]
      except:
          info[location]={row[0]:0}
          lastInfo=info[location]
      finally:
          
          try:
            lastValue=lastInfo[row[0]]       
            lastValue=int(lastValue)+int(row[2])
          except:
            pass
          lastInfo[row[0]]=lastValue
          info[location]=lastInfo      
info.pop('destination') 
print(info['0'])