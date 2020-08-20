# attendance
Automation tool for taking attendance

PREREQUISIT:  selenium & chromedriver

Automaion script to take attendance from google meet
Selenium and chromedriver are required --> refer: https://www.youtube.com/watch?v=eDrFWRi13DY
After script is started a google chrome window opens up and the user needs to authenticate his/her google account
however since the browser instance is running in automation mode google won't authenticate normally. To authenticate google account,
log into any website authenticated by google for example log into stackoverflow.com using your google account.
after successful log-in open paste the google meet link in the search bar and click the allow microphone "notification" first before dismissing the 
prompt. After the user logs in succesfully ask participants to type something in the comment box. The script will start to take note of attendace after 
a certain amount of time indicated in the terminal as time remaining.

Note: Time remaining should be edited as the default time window as buffer_time is 75 seconds and should be increased in order to provide the opportunity that everyone in the meeting responds. the command system('clear') doesn't work in windows environment. To make it work, just replace clear with 'cls'

Happy Logging ;)
