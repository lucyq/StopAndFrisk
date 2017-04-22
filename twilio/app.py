#import messageSender

from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import random
import atexit
import csv

# App Modules
import userManager

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


TWILIO_ACCOUNT_SID = "ACaaab3e6d6e25a9644e8289306d90c395"
TWILIO_AUTH_TOKEN = "cd1ea5b16e0e7c42bdfff8239be691e1"
TWILIO_NUM = "+16172022872"
TWILIO_MSG_ID = 'MG09846332b0012e9557d19ef6d7ac12ea'


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)



def sendMessageOfDay():
    all_users = userManager.getAllUsers()


    msg = getRandomEntry()    

    for user in all_users:
        print("Sending message to", user)
        client.messages.create(
                to="+" + user, 
                from_=TWILIO_NUM,
                body=msg
            )



    # now = datetime.datetime.now()

    # print(now)

  
    # print(daily_msg)    
    # all_users = userManager.getAllUsers()


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=sendMessageOfDay,
    # trigger=IntervalTrigger(seconds=86400)
    trigger=IntervalTrigger(seconds=2),
    id='printing job',
    name='testing123',
    replace_existing=True)

atexit.register(lambda: scheduler.shutdown())


INIT_MSG = "Hello {}, welcome!"

app = Flask(__name__)
userManager.loadData()

@app.route("/")
def displayIndex():
    return render_template('index.html')



@app.route('/init', methods=['POST'])
def sms():
    number = request.form['From'].strip('+')
    message_body = request.form['Body']
    resp = MessagingResponse()

    if userManager.isUser(number):
        print("User: {}, Message: {}".format(number, message_body))
        resp.message(getRandomEntry())
    else:
        print("New user: ", number);
        userManager.addUser(number)
        resp.message(INIT_MSG.format(number))

    return str(resp)


def getRandomEntry():
    file_path = "../data/StopAndFrisk-person.csv"

    suspicions = ["Reasonable Suspicion", "Probable Cause", "Intel"]
    actions = ["Stopped", "Observed","Encountered"]
    cities = ["Dorchester", "Boston", "Roxbury", "Jamaica Plain", "Mattapan", "Brighton"]

    msg = ""
    with open(file_path, 'rb') as csvfile:
        rdr = csv.reader(csvfile)
        row_count = sum(1 for row in rdr)
        rand_index = random.randrange(row_count)
        csvfile.seek(0)
        for i, row in enumerate(rdr):
            if i == rand_index:
                date = row[2]
                age = row[5]
                sex = row[3].lower()
                race = row[4].lower()
    
                msg = "On " + date + " police " + random.choice(actions).lower() +" a " + age + " year-old " + race + " " + sex + " in " + random.choice(cities) + " citing: " + random.choice(suspicions).lower()
                msg += "\n\nFind out more at http://stopfrisking.me"

    return msg








if __name__ == "__main__":
    app.run()



