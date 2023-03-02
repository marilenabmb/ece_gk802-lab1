import requests
import time
from datetime import timedelta

#asking user to insert a url
url = input("please enter a valid url:")

#making a get request
response = requests.get(url)

#getting and printing the headers
headers = response.headers.items()
print(headers)

#getting the os of the web server
for key, value in headers:
        if key=="Server":
            print("Server:",format(value))

#printing the name and expiration time of each cookie
if(response.cookies):
            for key,value in enumerate(response.cookies):
                print("{} {} {}".format(key,value,timedelta(seconds=(value.expires-time.time()))))
            
else:
        print("No cookies")
        print("Server:",format(value))
