#!/bin/python

import json
import requests
import os
import argparse
from slack import Slack, SlackMessage
from radarr import RadarrApi
from tmdb import TmdbApi

def _argparse():
    parser = argparse.ArgumentParser(
        description='Radarr Custom Script : perform Slack rich notification'
    )
    parser.add_argument(
        '--webhook-url', '-wu',
        help='Slack webhook url'
    )
    parser.add_argument(
        '--radarr-url', '-re',
        help='Radarr API endpoint : https://xxxx/api'
    )
    parser.add_argument(
        '--radarr-key', '-rk',
        help='Radarr API key, find it on Radarr > Settings > General'
    )
    parser.add_argument(
        '--tmdb-key', '-tk',
        help='TMDB API Key, register app on tmdb to obtain API Key'
    )
    parser.add_argument(
        '--tmdb-language', '-lg',
        help='TMDB language'
    )
    args = parser.parse_args()
    return args


args = _argparse()

movieId = os.environ.get("radarr_movie_id", "1")
eventType = os.environ.get("radarr_eventtype", "Download")
downloadId = os.environ.get("radarr_download_id", "1")
movieTmdbId = os.environ.get("radarr_movie_tmdbid", "12")
movieTitle = os.environ.get("radarr_movie_title", "Finding Nemo")
movieFileQuality = os.environ.get("radarr_moviefile_quality", "4k")
movieFileReleasegroup = os.environ.get("radarr_moviefile_releasegroup", "REGRET")
tmdbLanguage = args.tmdb_language if args.tmdb_language is not None else "fr-FR"

radarr = RadarrApi(args.radarr_url, args.radarr_key)
radarr.unmonitorMovieIfNeeded(movieId, eventType)
radarr.loadData(downloadId)
link = "https://www.themoviedb.org/movie/"+movieTmdbId+"?language="+tmdbLanguage

tmdb = TmdbApi(args.tmdb_key)
tmdb.loadMovieData(radarr.tmdbId)
tmdb.downloadMovieProductionImage()

message = SlackMessage(args.webhook_url)
message.package("*"+ movieTitle +"* ("+ radarr.year +") ["+ movieFileQuality +"]")
message.constructor("`" +radarr.indexer+"` _"+movieFileReleasegroup+"_ ("+radarr.sizeOnDisk+")")
message.link(link)
message.save()

message.notify()
