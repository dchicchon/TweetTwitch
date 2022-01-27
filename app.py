from dotenv import dotenv_values
from twypy.api import Api
import obspython as obs
from pathlib import Path

streaming = False
client = ''
start_tweet = ''
end_tweet = ''

class Data:
    _start_tweet_  = None
    _end_tweet_ = None
    _settings_ = None

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
    obs.obs_properties_add_text(props,'start_tweet','Start Tweet:', obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props,'end_tweet','End Tweet:', obs.OBS_TEXT_DEFAULT)
    return props

def script_update(settings):
    Data._start_tweet_ = obs.obs_data_get_string(settings, 'start_tweet')
    Data._end_tweet_ = obs.obs_data_get_string(settings, 'end_tweet')
    Data._settings_ = settings

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
    print(Data._start_tweet_)
    client.api.statuses.update.post(status=start_tweet) 

def send_end_tweet():
    print(Data._end_tweet_)
    client.api.statuses.update.post(status=end_tweet) 

