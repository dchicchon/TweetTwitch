from dotenv import dotenv_values
from twypy.api import Api

obs = obspython
streaming = False
client = ''
start_tweet = ''
end_tweet = ''
def script_description():
    return "Sending a tweet when stream starts and when stream ends"

def script_load(settings):
    global client
    print('script load')
    config = dotenv_values('.env')
    client = Api(config['TWITTER_API_KEY'], config['TWITTER_SECRET'],
                 config['TWITTER_ACCESS_TOKEN'], config['TWITTER_TOKEN_SECRET'])
    sh = obs.obs_get_signal_handler()
    obs.signal_handler_connect(sh, "source_activate", source_activated)
    obs.signal_handler_connect(sh, "source_deactivate", source_deactivated)

def script_properties():
    props = obs.obs_properties_create()
    start = obs.obs_properties_add_text(props,'start_tweet','Start Tweet:', obs.OBS_TEXT_DEFAULT)
    end = obs.obs_properties_add_text(props,'end_tweet','End Tweet:', obs.OBS_TEXT_DEFAULT)
    obs.obs_property_set_modified_callback(start , start_tweet_callback)
    obs.obs_property_set_modified_callback(end , end_tweet_callback)
    return props

def start_tweet_callback(props,prop, settings):
    # startElm = obs.obs_properties_get(props,"start_tweet")
    startText = obs.obs_data_get_string(settings,"start_tweet")
    print(startText)
    return True

def end_tweet_callback(props, prop, settings):
    endText = obs.obs_data_get_string(settings,"end_tweet")
    print(endText)
    return True

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

def send_start_tweet():

    print(start_tweet)
    client.api.statuses.update.post(status=start_tweet) 

def send_end_tweet():
    print(end_tweet)
    client.api.statuses.update.post(status=end_tweet) 

