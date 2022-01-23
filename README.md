
# Philips Hue Self Muted Discord Notification

Set a philips hue light source to red when you are self muted yourself in a discord channel.

## HOW-TO

Create a `.env` file with these necessary parameters:

* `DISCORD_TOKEN` to the bot.
* `IP_PHUE` local ip address to Philips Hue Bridge
* `INPUT_USERNAME` which user to act on 
* `LIGHT_SOURCE` which philips hue light source to use 

In additional, we need to create a local `.python_hue` config file, run `main.py` locally and then copy it from `$HOME/.python_hue` to the local path where you create the docker image. Remember, you need to press the button on the Philips Hue Bridge to sync the application and obtain the username for the config.

An example of the config, `.python_hue`:
```
{"192.168.X.X": {"username": "XXXXX"}}%   
```

To create the docker image, run `make build` and `make run` to run it locally.