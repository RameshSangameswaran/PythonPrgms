import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "gLvNBd1wEkIFQvcqh5vRc2UGs",
    "consumer_secret"     : "rooSskHWHbSu0Q4yuQbTlCmBaLaFjtXZpqD7vckfXRe321WteP",
    "access_token"        : "216357728-kje3FAAOfjdkiI61SasokKMTn7mKTorLM0Yxp3d1",
    "access_token_secret" : "PBuzA5dptQtuygVD14OEKvQniMb32taYk4uiJuVNKMZk3" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
