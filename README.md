
# Philips Hue Self Muted Discord Notification

Set a philips hue light source to red when you are self muted yourself in a discord channel.

## HOW-TO

Fill in the `.env` template with the necessary parameters:

* `DISCORD_TOKEN` to the bot.
* `IP_PHUE` local ip address to Philips Hue Bridge
* `INPUT_USERNAME` which user to act on 
* `LIGHT_SOURCE` which philips hue light source to use 

In additional, we need to create a local `.python_hue` config file, run `main.py` and copy it from `$HOME/.python_hue` to the local path where you create the docker image. To sync the app, you need to press the button on the Philips Hue Bridge to sync it.

An example of the config, `.python_hue`:
```
{"192.168.X.X": {"username": "XXXXX"}}%   
```