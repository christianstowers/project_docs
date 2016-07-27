import urllib2

response = urllib2.urlopen('http://www.politico.com/story/2016/07/full-transcript-donald-trump-nomination-acceptance-speech-at-rnc-225974')
html = response.read()

buzz = 0
list_of_words = html.split(' ')
for word in list_of_words:
	if word == 'Obama':
		buzz += 1

print buzz

		