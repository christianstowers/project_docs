#imports PRAW package
import praw

user_agent = ('Message Test Bot 0.1')
#creates the Reddit object
r = praw.Reddit(user_agent = user_agent)


#logs you in
"""
DeprecationWarning: reddit intends to disable password-based
 authentication of API clients sometime in the near future. 
 As a result this method will be removed in a future major 
 version of PRAW.
"""
#tried running without this(20052016). still required...for now.
r.login('wookieforhire', 'c0ff33')

#sends a message
r.send_message('wookieforhire', 'well hey there!', 'You\'ve been botted twice.')

print "////////////////////////////////////"

#gets subreddit top submissions
submissions = r.get_subreddit('motorcycles').get_top(limit=10)
#and this gets comments from a given submission
submission = next(submissions)
submission.comments