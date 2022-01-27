# TweetTwitch
When I start streaming on OBS Studio, I tweet! (hopefully)

## Prequisites
- Install [OBS Studio](https://obsproject.com/)
- [Install Python 3.6.8](https://www.python.org/downloads/release/python-368/). Make sure to download the Python version that matches your OBS Studio version (x64 or x32)
- Make sure that you have setup your project in the [Twitter API](https://developer.twitter.com/en/docs/twitter-api).
    - Ensure that you have set your permissions to allow for `read and write access`. It will require you to add a callback URI and website URL but since you will be using your own tokens you can list any website. If you cannot think of any, you can use `https://example.com`

## Installation
1. Install dependencies
```
pip install -r requirements.txt
```
2. Add your .env file to this directory `C:/Program Files/obs-studio/bin/64bit`. Ensure that the file is still called `.env`

3. In the scripts menu, there should be a tab for Python Settings. Link the path to your python directory here. Should look like `C:/Users/danie/AppData/Local/Programs/Python/Python36`

4. Load your script in the `Tools > scripts` menu in OBS Studio. 

5. Make sure to have more than 1 scene in your stream. Once you start streaming and then switch scenes then you will tweet out your stream!



## Video Tutorial
// insert link here when i do the tutorial