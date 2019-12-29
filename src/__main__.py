#!/usr/bin/env python3
import redditwatchdog
import emailclient

def main():
    email = emailclient.emailClient('instarawr@gmail.com', 'sr3slkrs5')
    email.set_target(['6092802504@txt.att.net'])
    try:
        email.connect()
    except Exception as err:
        print(err)
        exit(1)

    watchdog = redditwatchdog.redditWatchdog('ixslrIj5YFlrQA','k0uIDjyC-HLRZCu3ju3Bke4b5ok','android:com.example.myredditapp:v1.2.3 (by /u/cashmen)')
    while 1:
        try:
            watchdog.submission_comment_watchdog('eh32t3', notifyFunc=email.email_send)
        except Exception as err:
            print(err)
            print("Restarting watchdog")

if __name__ == "__main__":
    main()
