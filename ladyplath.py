twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

gagafile = open("gaga.txt", "rb")

gagalines = gagafile.readlines()

gagalines = [elem for elem in gagalines if len(elem) <= 70 and len(elem) > 7]

plathfile = open("plath.txt", "rb")

plathlines = plathfile.readlines()

plathlines = [elem for elem in plathlines if len(elem) <= 70 and len(elem) > 7]

plathtweet = random.choice(plathlines)    

gagatweet = random.choice(gagalines)

randomchoice = [1,2]

tweetorder = random.choice(randomchoice)

if tweetorder == 1:
    tweet = "%s %s" % (plathtweet, gagatweet)
    twitter.update_status(status=tweet)
    
else:
    tweet = "%s %s" % (gagatweet, plathtweet)
    twitter.update_status(status=tweet) 

    
  