from twitter_bot import Scaper,AutoTwit

URL = "https://bhagavadgita.io/verse-of-the-day/"
TWITTER_URL = "https://twitter.com/i/flow/login"

#execute programme
def run_programme():
    scrp =Scaper(URL)
    do_tweet = AutoTwit(scrp)
    do_tweet.login(TWITTER_URL)
    do_tweet.tweet()
try:
    run_programme()
except TimeoutError :
    print("time out error occured. Reattempting")
    run_programme()