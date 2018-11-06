import credentials as creds
import praw
import datetime as dt
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
 # submission.comments.replace_more(limit= None)    #find way to get all necessary comments (max comments not some)

comments = submission.comments

df_rows = [[comment.parent, comment.id, comment.score, comment.created, comment.body ] for comment in comments]
df = pd.DataFrame (df_rows, columns = ['Parent ID', 'Comment ID', 'Score', 'Created', 'Body'])

print("Extraction Complete")

print("What would you like extraction file to be named? (Remember to add .csv)")
filename = str(input())

df.to_csv(filename)





