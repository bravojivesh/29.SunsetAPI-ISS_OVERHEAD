import requests
import smtplib
import datetime as dt
import pytz
#need this to covnert current time to GMT

import time

my_loc={"lng":85.323959, "lat":27.717245,"formatted":0}

def iss_close_enough():
    iss_api=requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_api.raise_for_status()

    data=iss_api.json()
    print (data)

    iss_long=float(data["iss_position"]["longitude"])
    iss_lat=float(data["iss_position"]["latitude"])

    print (f"the iss long lat is : {iss_long} and {iss_lat}\nMine is {my_loc['lng']} and {my_loc['lat']}")

    if iss_lat>my_loc["lat"] or iss_long>my_loc["lng"]: #this is all me. So that I can test the code. It should be \
        # greater or smaller than 5
        return True

def is_dark():
    api_sunrise_sunset=requests.get(url="https://api.sunrise-sunset.org/json", params=my_loc)
    data=api_sunrise_sunset.json()
    print (data)

    sunrise_ref=data["results"]["sunrise"].split("T")[1].split(":")[0]
    #to get the sunrise hour. First split time from date. And then hour from time.
    sunset_ref = data["results"]["sunset"].split("T")[1].split(":")[0]
    # to get the sunset hour. First split time from date. And then hour from time.
    print(f"The sunrise hour in GMT is {sunrise_ref},and the sunset is {sunset_ref}")

    curr_time0=dt.datetime.now()
    curr_time=curr_time0.astimezone(pytz.timezone("GMT"))
    #covert the current time to GMT because ISS time is in GMT
    print(f"The current time before conversion is: {curr_time} and the type is {type(curr_time)}") #raw datetime

    curr_time_after=int(str(curr_time).split(" ")[1].split(":")[0])
    #first change the datetime to string. Split to get time. And then split time to get the hour. And finally
    # convert it into integer so that we can compare later on.
    print(f"The current time after conversion is: {curr_time_after} and the type is {type(curr_time_after)}") #raw datetime

    if curr_time_after >=int(sunset_ref) or curr_time_after<=int(sunrise_ref):
        print ("It's dark")
        return True


# while True:
#     time.sleep(60)
# uncomment this and indent if you want the code to run ever 60 secods. I actually dont need. this.
if iss_close_enough() and is_dark():
    my_email = "bravojivesh@gmail.com"
    my_password = "tfyqlfluvzvezaqb"
    message = f"It is getting closer foo + {dt.datetime.now()}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("i am here")  # debgging
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="hamal.jivesh@gmail.com",
                            msg=f"Subject:YOOO\n\n {message}")
            # using f strings for the message
