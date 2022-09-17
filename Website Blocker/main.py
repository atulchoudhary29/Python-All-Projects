import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com ", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): # Condition for Working Hours
        with open(hosts_path,'r+') as file:
            content=file.read() # Opens Host File as read+Write Mode
            for website in website_list:
                if website in content: # Checking that Websites is in the file or not.
                    pass
                else:
                    file.write(redirect+"   "+website+"\n") # Write in the file.
    else:
        with open(hosts_path,'r+') as file:# Opens the file.
            content=file.readlines() # Read file line by line.
            file.seek(0) # Pointer goes to Starting Point of file.
            for line in content:
                if not any(website in line for website in website_list): #Checking that Websites is in the file and append the original file without websites.
                    file.write(line)
            file.truncate() # Deleted the Websites list.       