Hi there,

I created a short python script to find out when vaccine slots are available. Part of the code I used is taken from the code available on internet. So cheers to that guy (Bhavesh I think).

My code does the following things which are new:

1. Works solely on python and checks for slots constantly in the background.
2. Sends an email as soon as slots are detected for your age group. Works on basis of pincode.
3. Email consists of name of places, dates and the type of vaccine, along with the availability.
4. Automatically opens the cowin website on your desktop browser as soon as slots are detected.
5. Sleep is added as there is a limit of 100 API calls in 5 mins for CoWin.

P.S. A short hyperlink is provided in each email for your convenience.

Steps to use:

1. Download the given script and modify the age, pincode, email addresses of sender and receiver (you can keep same if you want to send yourself), password of gmail account.
2. Make sure you have python installed along with all the necessary modules which are at the top (Starts with import).
3. In case you dont have modules, download them using pip. The command is as follows: pip install module_name
4. You can find pip in you python folder> Scripts.
5. I used python 3.8 version for this.
6. If you're unable to receive emails, go to gmail account > manage your account option > Security > Allow less secured apps, turn it on. (It might be off by default).
7. To run the code, open it in Python IDLE (after doing above steps) and press F5 to run module, you can keep it minimized now and web browser will automatically open cowin website and mail will be automatically sent to your email as soon as it senses that slots are available. If you close it, you need to restart it again for it to work.

P.S. Adjust the sleep timer (t.sleep=54) in code accordingly if you're unable to send requests (i.e. if you're facing request failed, increase the timer to 60 or 70)

Feel free to modify it further. Thanks.
