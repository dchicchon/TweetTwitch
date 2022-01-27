from dotenv import dotenv_values
from twypy.api import Api

obs = obspython
streaming = ''
client = ''

def script_load(settings):
    global client
    global streaming
    print('script load')
    config = dotenv_values('.env')
    streaming = False
    client = Api(config['TWITTER_API_KEY'], config['TWITTER_SECRET'],
                 config['TWITTER_ACCESS_TOKEN'], config['TWITTER_TOKEN_SECRET'])
    sh = obs.obs_get_signal_handler()
    obs.signal_handler_connect(sh, "source_activate", source_activated)
    obs.signal_handler_connect(sh, "source_deactivate", source_deactivated)

def source_activated(cd):
    global streaming
    if obs.obs_frontend_streaming_active() and streaming != True:
        streaming = True
        send_start_tweet()

def source_deactivated(cd):
    global streaming
    if not obs.obs_frontend_streaming_active() and streaming:
        streaming = False
        send_end_tweet()

def send_end_tweet():
    tweet = 'Ending Coding Stream!'
    print(tweet)
    client.api.statuses.update.post(status=tweet) 

def send_start_tweet():
    tweet = 'Starting Coding Stream! Check it out here: https://www.twitch.tv/dannychicchon'
    print(tweet)
    client.api.statuses.update.post(status=tweet) 

def script_description():
    return "Sending a tweet when stream starts and when stream ends"