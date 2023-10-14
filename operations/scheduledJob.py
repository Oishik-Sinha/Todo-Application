from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime, date

from utilities import *


def sendMail():
    from todoManagement.models import todoTaskList

    tasks = todoTaskList.objects.filter(deadline__startswith = date.today(), one_day_notification = False)
    if tasks:
        for i in tasks:
            try:
                message = MIMEMultipart('alternative')
                message['Subject'] = f'Today You Have a Deadline for {i.name}'
                message['From'] = 'noreply.todotask@gmail.com'
                message['To'] = f"{i.user.email}"
                message.attach(MIMEText(f'<h1>Task Name : {i.name}</h1> <h4>Description</h4> <p>{i.description}</p> <h1>Dead Line : {datetime.datetime.strftime(i.deadline, "%Y-%m-%d %H:%M:%S").split("+")[0]}</h1>', 'html'))
                s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

                s.ehlo()  
                s.login("noreply.todotask@gmail.com", "xmwr wzsd vnsw zytp")
                s.sendmail("noreply.todotask@gmail.com", f"{i.user.email}", message.as_string())

                # terminating the session
                s.quit()

                data = {'updatedAt': datetime.datetime.now(), 'one_day_notification': True}
                todoTaskList.objects.filter(pk=i.pk).update(**data)
                
            except Exception as e:
                print(str(e))