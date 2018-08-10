import requests
import json
import os
import datetime

#day=09&month=08&year=2018&name=Despacito&hour=07&minute=30&duration=1hr&netlinkid=salphonso&netlinkpw=wh1t3Wh4le&returl=&room_id=15&create_by=

#

postData = {'day':'00',
            'month':'00',
            'year':'00',
            'name':'StudyBois',
            'hour':'08',
            'minute':'00',
            'duration':'2hr',
            'netlinkid':'',
            'netlinkpw':'',
            'returl':'',
            'room_id':'15',
            'create_by':''
            }


cur_path =  os.path.dirname(os.path.realpath(__file__)) + '/netlinkIDs.json'

with open(cur_path) as file:
    logins = json.load(file)

today = datetime.date.today()
nextBookingDay = today

nextBookingDay = today + datetime.timedelta(days=7)
dayShift = nextBookingDay.day % 2

postData['day'] = nextBookingDay.strftime('%d')
postData['month'] = nextBookingDay.strftime('%m')
postData['year'] =nextBookingDay.strftime('%Y')
postData['hour'] = 11 - (dayShift)

url = 'https://webapp.library.uvic.ca/studyrooms/edit_entry_handler.php'


i = 0
for username, password in zip(logins['usernames'], logins["passwords"]):


            postData['hour'] = postData['hour']+ (i*4)
            postData['netlinkid'] = username
            postData['netlinkpw'] = password

            requests.post(url, allow_redirects=False, data=postData)

            i += 1
