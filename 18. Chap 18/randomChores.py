import random
import json
import smtplib

# smtp google info 
myEmail = 'asfasdf@gmail.com'
myPassword = 'secretPassword'

# recipient addr and chores

emailAddr = ['one@email.com', 'two@email.com', 'three@email.com', 'four@email.com']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# open txt file with last week's chores in a dict
with open('last_week_chrores.json','r') as last_week_chores_text:
    last_week_chores = json.load(last_week_chores_text)
    this_week_chores = {}

    # random assign chores, remove after assignment
    while True:
        temp_chore_list = chores[:]
        for email in emailAddr:
            selected_chore = random.choice(temp_chore_list)
            this_week_chores[email] = selected_chore
            temp_chore_list.remove(selected_chore)
        # checkfor repeats from prior week by checking if there any overlap
        if not this_week_chores.items() and last_week_chores.item():
            break

        #login SMTP 

        smtpObj = smtplib.SMTP('smtp.gmail.com' , 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(myEmail, myPassword)

        # email new chore list to reciptients

        for repcipient_email, chore in this_week_chores.items():
            smtpObj.sendmail(from_addr=emailAddr, to_addrs=repcipient_email, msg=f'Subject: Testing.\n {chore}')


    # save this week's chores
    with open('last_week_chores.json' , 'w') as last_week_chores_update:
        json_file = json.dump(this_week_chores, last_week_chores_update,indent=2)        

