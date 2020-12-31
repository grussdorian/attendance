# attendance
Automation tool for taking attendance on Google Meet

**PREREQUISITE** 

1. Python interpreter

2. Selenium

3. Chromedriver

**About**

selenium & Chromedriver Automation script to take attendance from google meet
refer: https://www.youtube.com/watch?v=eDrFWRi13DY 
After script is started a google chrome window pops up and the user needs to authenticate his/her google account.
However the browser instance is running in automation mode google won't authenticate normally.
To authenticate google account, log into any website authenticated by google for example log into stackoverflow.com using your google account.
After successful log-in open, paste the google meet link in the search bar and click the allow microphone "notification" first before dismissing the prompt.
After the user logs in successfully ask participants to type something in the comment box. The script will start to take note of attendance after a certain amount of time indicated in the terminal as time remaining.
The output is generated as a text file in the same directory as the script.

**Note** Time remaining should be edited as the default time window as buffer_time is 75 seconds and should be increased in order to provide the opportunity that everyone in the meeting responds. The command system('clear') doesn't work in windows environment. To make it work, just replace clear with 'cls'Happy Logging ;)

**Run**
```console
foo@bar:~/Attendance$ python3 attendance.py
```
