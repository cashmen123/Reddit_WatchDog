#!/usr/bin/env python3
import smtplib

class emailClient:
    username = None
    password = None
    emailServer = None
    target = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connect()

    def set_target(self, target):
        self.target = target

    def connect(self):
        print("Attempting to connect to gmail")
        self.email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.email_server.ehlo()
        self.email_server.login(self.username, self.password)

    def email_send(self, body):
        try:
            print(self.email_server.sendmail(self.username, self.target, body))
            print("Sent: {}".format(body))
        except smtplib.SMTPSenderRefused:
            try:
                self.connect()
                print(self.email_server.sendmail(send_from, to, body))
                print("Sent email")
            except:
                print("Failed to send email.")

