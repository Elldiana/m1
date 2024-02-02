from datetime import datetime
from datetime import timedelta


dimdi = datetime.now()

result = datetime.now()
result = dimdi.year
result = dimdi.month
result = dimdi.day
result = dimdi.hour
result = dimdi.minute
result = dimdi.second

result = datetime.ctime(dimdi)
result = datetime.strftime(dimdi, "%Y")  # Year
result = datetime.strftime(dimdi, "%X")  # Hour
result = datetime.strftime(dimdi, "%d")  # Day
result = datetime.strftime(dimdi, "%A")  # week
result = datetime.strftime(dimdi, "%B")  # Month
result = datetime.strftime(dimdi, "%M")  # Minute
result = datetime.strftime(dimdi, "%Y %B %A")  # Year, Month, week

birthday = datetime(1999,10,25,23,35,10) # kendimşz uyuşturan tarih
result = dimdi - birthday

apam1 = datetime(1959,2,10)
apam0 = datetime(2023,5,15)
result = apam0 - apam1
result =  dimdi - apam0 


mam = datetime(1977,7,31)
result = dimdi - mam

ejem = datetime(1992,5,19)
result = dimdi - ejem

has = datetime(1976,7,24)
result = dimdi - has

#  ********************
ai = datetime(2010,9,20)
result = dimdi - ai

al = datetime(2011,10,18)
result = dimdi - al

ais = datetime(2013,7,18)
result = dimdi - ais

az= datetime(2015,12,9)
result = dimdi - az

# result = dimdi + timedelta(days = 10) # 10 gün ekledik neden???



print(result)
