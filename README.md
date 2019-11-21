# Radarr-CS

Radarr-CS is a custom script to send a notification to slack when radarr download, upgrade or rename a movie.

## Installation

Clone this repo to your local machine using:

```bash
git clone https://gitlab.com/buttice.j/radarr-cs.git
```

## Usage

**Go to `radarr` > `Settings` > `Connect` > `Add Custom script`**

> Name `Named this script`

> On Grab `no`

> On Download `yes`

> On Upgrade `yes`

> On Rename `yes`

> Path `/where-the-script-is/main.py`

> Arguments `-wu https://hooks.slack.com/services/xxx/xxx/xxx -re http://radarr-ip:port/api -rk 8xxxxxxxxxxxxxxxxc -tk fxxxxxxxxxxxxxxxxxxxxxxxxxx5`

**Arguments explanation**

Slack webhook url, create it on `https://my.slack.com/services/new/incoming-webhook/`

> -wu https://hooks.slack.com/services/xxx/xxx/xxx

Radarr API endpoint

> -re http://radarr-ip:port/api

Radarr API key, find it on Radarr > Settings > General

> -rk 8xxxxxxxxxxxxxxxxc

TMDB API Key, register app on tmdb to obtain API Key

> -tk fxxxxxxxxxxxxxxxxxxxxxxxxxx5
