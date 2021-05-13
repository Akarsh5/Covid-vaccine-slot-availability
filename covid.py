import time as t
from time import sleep
from datetime import datetime, time
import datetime
import json
import requests
from fake_useragent import UserAgent
import webbrowser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


pincode = "302039"
age = 52
message_body=""
temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

print_flag = 'N'

numdays = 20

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
count = 0
browser = 0
s_mail=0

def send_mail():
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "your_password"
    global message_body
    message = MIMEMultipart("alternative")
    message["Subject"] = "Covid-19 Slot Available!"
    message["From"] = "sender@gmail.com"
    message["To"] = "receiver@gmail.com"
    
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
            sender_email, receiver_email, message.as_string()
        )


def covid():
            for vaccine_date in date_str:
                global count
                global browser
                global s_mail
                global message_body
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, vaccine_date)
                response = requests.get(URL, headers=browser_header)
                count+=1
                #print(response)
                #print(response.text)
                if response.ok:
                    resp_json = response.json()
                    if (response.ok) and ('centers' in json.loads(response.text)):
                        print("Got response. Checking...")
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

            if s_mail==1:
                    print("Sending mail...")
                    send_mail()
                    s_mail=0

            if count==20:
                    print("Sleeping...")
                    message_body=""
                    count=0
                    t.sleep(54)
                    browser=0
                    covid()
covid()               
