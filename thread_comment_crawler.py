import credentials as creds
import praw
import pandas as pd
from pandas import DataFrame


print("Authenticating...")
r = praw.Reddit(username = creds.username, password = creds.password, client_id = creds.client_id,
                client_secret = creds.client_secret, user_agent = creds.user_agent)

print("Reddit credentials have been accepted")


print("Please input the Submission ID of the Thread that you would like to scrape.")
print("Submission ID can be found in URL: 'wwww.reddit.com/r/subreddit-name'/comments/'submission-id'")
submission_id = str(input())

print("Extracting...")
submission = r.submission(id = submission_id)

postlist = []

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    post = {}
    post['Author'] = comment.author
    post['Comment'] = comment.body
    postlist.append(post)

df = pd.DataFrame(postlist)
print("Extraction Complete")

print("What would you like extraction file to be named? (Remember to add .csv)")
filename = str(input())

df.to_csv(filename)




