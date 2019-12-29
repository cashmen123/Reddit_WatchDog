#!/usr/bin/env python3
import praw
import time

class redditWatchdog:
    redditclient = None

    def __init__(self, client_id, client_secret, user_agent):
        self.redditclient = praw.Reddit(client_id=client_id,
                                   client_secret=client_secret,
                                   user_agent=user_agent)
        print("Watchdog initialized")

    def submission_comment_watchdog(self, submissionid, notifyFunc = None):
        print("Watching thread ID: {}".format(submissionid))
        already_done = set()
        existed = 0
        count = 0
        while 1:
            submission = self.redditclient.submission(id=submissionid)
            submission.comments.replace_more(limit=None)
            forest_comments = submission.comments
            flat_comments = forest_comments.list()
            for comment in flat_comments:
                if comment.id not in already_done:
                    if existed != 0:
                        print("Comment count: {}".format(len(flat_comments)))
                        commentdata = "New comment by user {}\n{}".format(comment.author, comment.body)
                        if notifyFunc:
                            notifyFunc(commentdata)
                    already_done.add(comment.id)
            if existed == 0:
                existed = 1
            time.sleep(5)

