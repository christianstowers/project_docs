#import PRAW pkg
import praw

master_jedi = ("PyNoob Moto 0.1")

#create a Reddit object
r = praw.Reddit(client_id = "Fv3S7MmLuls-oQ",
				client_secret = "SfrSLmkZNOMcfkEgyShq7GK-85w",
				user_agent = "master_jedi",
				username = "PyNoob Moto 0.1")

#this isn't working yet. "'Reddit' has not attribute 'get_subreddit'".
#since updating to praw 5.1. 
subreddit = r.get_subreddit("motorcycle")

for submission in subreddit.get_hot(limit = 10):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print "\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"