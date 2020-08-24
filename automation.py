from selenium import webdriver
import time
import datetime
from collections import OrderedDict as od
from os import system
Chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
Chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('/home/hardik/Desktop/attendance/chromedriver',options=Chrome_options)


#names ordered dictionary

names_dict = od({
"hardik ghoshal": 90,
"priyanka bepari": 137,
"dwipanjana das": 140,
"memo karpa": 178,
"anwesha sardar": 289,
"goutam biswas": 306,
"jayanta sarkar":308,
"arian yeasin": 320,
"akash saha": 340,
"subhajit majumdar": 369,
"rupam das": 542,
"sourjaya das":556,
"atanu chakraborty": 559,
"daita sarkar" : 546,
"bhargab roy" : 610,
"arunabha dutt":613,
"santanu mondal": 618,
"tanamrita saren": 740,
"sattwik bal": 742,
"debasis paul": 744,
"hamza hasan": 815,
"sagnik dutta": 816,
"kushal das": 823,
"shruti jaiswal": 885,
"tamaghna bose": 1135,
"swaraj haldar": 1136,
"disha ganguly": 1139,
"subham de": 1140,
"sayan sarkar": 1143,
"santosh kumar yadav": 1144,
"arnab dey": 1148,
"parama mukherjee": 1151,
"hritick jaiswal": 1153,
"bishakha das": 1155,
"subhrojeet das": 1159,
"arifa saba": 1167,
"ayush chakraborty": 1277,
"maisha khatoon": 1178,
"asmita mukherjee": 1182,
"suprovo das": 1287,
"shruti shovan das": 1291,
"sneha das": 1292,
"chandrabrata biswas": 1306,
"anweshan roy chowdhury": 1307,
"sayon roy": 1346,
})


###########################
#
# ADD your real names here
#
###########################
def alias(name):
    if name=='sayonr':
        return 'sayon roy'
    elif name == 'sarah':
        return 'tanamrita saren'
    elif name == 'santosh kumar':
        return 'santosh kumar yadav'
    else:
        return name


buffer_time = 180
for i in range(0,buffer_time):
    system('clear')
    print('Time remaining = '+ str(buffer_time-i) + ' seconds', )
    time.sleep(1)

names_set = {"hardik ghoshal"}
#length = len(names_dict)+1
length = 1000
try:
    for i in range(1,length):
        name = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[1]/div[' + str(i) + ']/div[1]/div[1]').text.lower()
        name = alias(name)
        names_set.add(name)
except:
    print('Done')

print(names_set)
f = open("attendance.txt","w")
x = datetime.datetime.now().date()
f.write("\n"+ str(x) + "\n\n" )
nameIndentChars = 8
presentIndentChars = 24
for name in names_dict:
    if name in names_set:
        roll = str(names_dict[name])
        namechar = len(name)
        rollchar = len(roll)
        f.write(roll + (nameIndentChars-rollchar)*" " + name + (presentIndentChars-namechar)*" " + "Present\n")
    else:
        roll = str(names_dict[name])
        namechar = len(name)
        rollchar = len(roll)
        f.write(roll + (nameIndentChars-rollchar)*" " + name + (presentIndentChars-namechar)*" " + "Absent\n")
f.close()
driver.close()
