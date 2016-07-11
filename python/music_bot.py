#imports the PRAW package
import praw


user_agent = ("PyNoob Music Bot 0.1")
#creats a Reddit object
r = praw.Reddit(user_agent = user_agent)

#
subreddit = r.get_subreddit("futurebeats")

for submission in subreddit.get_hot(limit = 10):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print "<<<<---------------------|||----------------------->>>>"
	