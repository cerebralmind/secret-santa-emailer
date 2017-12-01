#!/usr/bin/env python3.6.1
from image_text import gen_image

import smtplib
from string import Template
import uuid
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header

def santa_email(giver, giver_email, receiver, sig_other, price_limit='$50', config=None):
    email_credentials = config.email
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(email_credentials['username'], email_credentials['password'])

    image_path = gen_image(giver, receiver, config)
    img = dict(title=u'secret santa...', path=image_path, cid=str(uuid.uuid4()))
    sub_dict = {'giver': giver, 'receiver': receiver, 'sig_other': sig_other, 'price_limit': price_limit, 'cid': img['cid']}

    msg = MIMEMultipart('related')
    msg['Subject'] = Header(u'Your Secret Santa Partner (For your eyes only)', 'utf-8')
    msg['From'] = email_credentials['username']
    msg['To'] = giver_email
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    plain_body_of_email = Template(open('email_template.txt').read()).safe_substitute(sub_dict)
    msg_text = MIMEText(plain_body_of_email, 'plain', 'utf-8')
    msg_alternative.attach(msg_text)

    html_body_of_email = Template(open('email_template.html').read()).safe_substitute(sub_dict)
    msg_html = MIMEText(html_body_of_email, 'html', 'utf-8')
    msg_alternative.attach(msg_html)

    with open(img['path'], 'rb') as file:
        msg_image = MIMEImage(file.read(), name=os.path.basename(img['path']))
        msg.attach(msg_image)
    msg_image.add_header('Content-ID', '<{}>'.format(img['cid']))


    session.sendmail(email_credentials['username'], giver_email, msg.as_string())


