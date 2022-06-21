from datetime import datetime as dt
import datetime
import time

hosts_path = r"C:\\Windows\system32\drivers\etc\hosts" # Hosts file from System 
hosts_temp = r"C:\Users\HP\Desktop\Python\website_blocker\hosts" # Temp.Hosts file copied from System 
redirect = "127.0.0.1"
websites_list = ["www.facebook.com","www.netflix.com"]

while True:
    if datetime.time(8,00)<=dt.now().time()<= datetime.time(18,00):
        #print('Working Hours')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in websites_list:
                if website not in content:
                    file.write(redirect+" " + website+"\n")
    else:
        #print('Fun time')
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)