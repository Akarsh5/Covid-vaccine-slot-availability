Hi there,

I created a short python script to find out when vaccine slots are available. Part of the code I used is taken from the code available on internet. So kudos to him (Bhavesh Bhatt).

My code does the following things which are new:

1. Works solely on python and checks for slots constantly in the background.
2. Sends an email as soon as slots are detected for your age group. Works on basis of pincode.
3. Email consists of name of places, dates and the type of vaccine, along with the availability.
4. Automatically opens the cowin website on your desktop browser as soon as slots are detected.
5. Sleep is added as there is a limit of 100 API calls in 5 mins for CoWin.

P.S. A short hyperlink is provided in each email for your convenience.

Steps to use:

1. Download the given script and requirements file.
2. Make sure you have python installed. Place all the downloaded files in a folder and install all requirements using: pip install -r requirements.txt
3. In case you still have difficulty with modules/requirements/imports, download them using pip. The command is as follows: pip install module_name
4. You can find pip in you Python folder > Scripts. OR open cmd and type pip
5. I used python 3.8 version for this.
6. If you're unable to receive emails, go to gmail account > manage your account option > Security > Allow less secured apps, turn it on. (It might be off by default).
7. Double click covid.py file to run the code OR open it in Python IDLE (after doing above steps) and press F5 to run module. Type the age, pincode, email addresses of sender and receiver (you can press enter to keep same if you want to send yourself), password of gmail account (password will be hidden so make sure you type it correctly). 
8. You can keep it minimized now and web browser will automatically open cowin website and mail will be automatically sent to your email as soon as it senses that slots are available. If you close it, you need to restart it again for it to work.
9. Make sure your internet connection is working in order to send a mail and laptop/pc is not off. Keep it on for the script to work.

P.S. Adjust the sleep timer (t.sleep=57) in code accordingly if you're unable to send requests (i.e. if you're facing request failed, increase the timer to 60 or 70)

Feel free to modify it further. Thanks.
