Hi there,

I created a short python script to find out when vaccine slots are available. The code present is a modified version of the code available on internet.

My code does the following things which are new:

1. Works solely on python and checks for slots constantly in the background.
2. Sends an email as soon as slots are detected for your age group. Works on basis of pincode.
3. Email consists of name of places, dates and the type of vaccine, along with the availability.
4. Automatically opens the cowin website on your desktop browser as soon as slots are detected.
5. Sleep is added ad there is a limit of 100 API calls in 5 mins for CoWin.

P.S. A short hyperlink is provided in each email for your convenience.

Steps to use:

1. Download the given script and modify the age, pincode, email addresses of sender and receiver (you can keep same if you want to send yourself), password of gmail account.
2. Make sure you have python installed along with all the necessary modules which are at the top (Starts with import).
3. In case you dont have modules, download them using pip. The command is as follows: pip install module_name
4. You can find pip in you python folder> Scripts.
5. I used python 3.8 version for this.
6. If you're unable to receive emails, go to gmail account > manage your account option > Security > Allow less secured apps, turn it on. (It might be off by default).

P.S. Adjust the sleep timer (t.sleep=54) accordingly if you're unable to send requests (i.e. if you're facing request failed, increase the timer to 60 or 70)