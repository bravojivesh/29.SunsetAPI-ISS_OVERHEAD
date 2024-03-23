import requests
import datetime as dt

# parameters=[27.717245,85.323959]
parameters={"lat":27.717245,"lng":85.323959,"formatted":0}
#go through the API doc to know which params are mandatory. Above long and lat are mandatory.

request1=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
request1.raise_for_status()

data=request1.json()

sunrise=data["results"]["sunrise"]
sunrise_hour=sunrise.split("T")[1].split(":")[0]
#first split will separate date with time.
#second split will seprate hours with mins,secs 

sunset=data["results"]["sunset"]
print (sunrise)
print (sunset)
print ("the hour only:",sunrise_hour,)


time_now1=dt.datetime.now()
print (time_now1)
