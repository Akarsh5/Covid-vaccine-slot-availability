import time as t
from time import sleep
from datetime import datetime, time
import datetime
import json
import requests
import getpass
from fake_useragent import UserAgent
import webbrowser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pincode =input("Enter your pincode: ")
age = int(input("Enter your age: "))
print("Both sender and receiver emails can be yours if you want to send the notification email to yourself.")
print("Please ensure sender email is by gmail.")
sender_email = input("Enter Sender Email ID: ")
password = getpass.getpass("Enter Sender Email ID Password (Input will be hidden, type correctly!) : ")
print("Press Enter if Sender and Receiver emails are the same else type Reveiver email. If not same, sender will be in cc.")
receiver_email = input("Enter Receiver Email ID: ") or sender_email
message_body=""
temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

print_flag = 'N'

numdays = 16

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
count = 0
browser = 0
s_mail=0
found=0
cc=""

def send_mail():
    global sender_email
    global receiver_email
    global password
    global message_body
    global cc
    message = MIMEMultipart("alternative")
    message["Subject"] = "Covid-19 Slot Available!"
    message["From"] = sender_email 
    message["To"] = receiver_email
    rcpt=[receiver_email]
    if sender_email != receiver_email:
        message["Cc"] = sender_email
        rcpt=[receiver_email,sender_email]
    html = """\
    <html>
      <body>
        <p>Hi,<br>
        <br>
           <a href="https://selfregistration.cowin.gov.in/">Covid slots</a> are now available at the following dates:<br>
           <br>
           {message_body}
           <br>
           Regards,<br>
           Akarsh Gupta<br>
           <br>
           
        </p>
      </body>
    </html>
    """.format(message_body=message_body)

    part = MIMEText(html, "html")
    message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, rcpt, message.as_string()
        )


def covid():
            for vaccine_date in date_str:
                global count
                global browser
                global s_mail
                global message_body
                global found
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, vaccine_date)
                response = requests.get(URL, headers=browser_header)
                count+=1
                #print(response)
                #print(response.text)
                if response.ok:
                    resp_json = response.json()
                    if (response.ok) and ('centers' in json.loads(response.text)) and resp_json is not None:
                        print("Got response. Checking for "+str(format(vaccine_date))+" (Current time: "+str(datetime.datetime.now().time())+")")
                        print_flag = 'y'
                        json_data = json.loads(response.text)
                        if(print_flag=='y' or print_flag=='Y'):
                            #print("stuck 101")
                            for center in resp_json["centers"]:
                                #print("stuck 102")
                                for session in center["sessions"]:
                                    #print("stuck 103")
                                    if (session["min_age_limit"] <= age) and (session["available_capacity"] > 0):
                                        #print("stuck 104")
                                        found=1
                                        print("Available on: "+str(format(vaccine_date))+" "+str(center['name'])+" "+str(center["block_name"])+" Price: "+str(center["fee_type"])+" Available Capacity: "+str(session["available_capacity"])+" Vaccine: "+str(session["vaccine"])+"\n")               
                                        message_body+="Available on: "+str(format(vaccine_date))+" "+str(center['name'])+" "+str(center["block_name"])+" Price: "+str(center["fee_type"])+" Available Capacity: "+str(session["available_capacity"])
                                        if(session["vaccine"] != ''):
                                            message_body+=" Vaccine: "+str(session["vaccine"])+"\n\n <br> <br>"
                                        if browser==0:
                                            s_mail=1
                                            browser=1
                                            webbrowser.open('https://selfregistration.cowin.gov.in/', new=2)
                                     
                            
                    else:
                        print("No available slots on {}".format(vaccine_date))
                        
                else:
                    print("req failed")
                    t.sleep(5)
                    covid()

                if found==1:
                    found=0
                else:
                    print("No slots available on {}".format(vaccine_date))

            if s_mail==1:
                    print("Sending mail...")
                    send_mail()
                    s_mail=0

            if count==16:
                    print("Sleeping...")
                    message_body=""
                    count=0
                    t.sleep(57)
                    browser=0
                    covid()

covid()
