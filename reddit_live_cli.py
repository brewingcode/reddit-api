#!/usr/bin/env python

import requests
import os
import sys
import json
import arrow
import time

def unpack_creds():
    env_var = os.environ['REDDIT_LIVE_CREDS']
    sep_char = env_var[0]
    return env_var[1:].split(sep_char)

def api_request(url):
    user_agent = "reddit-live-cli/0.1"
    app_id, app_secret, username, password = unpack_creds()
    client_auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
    post_data = {"grant_type": "password",
        "username": username,
        "password": password}
    headers = {"User-Agent": user_agent}
    response = requests.post("https://www.reddit.com/api/v1/access_token",
        auth=client_auth, data=post_data, headers=headers)
    token = response.json()['access_token']
    headers = {"Authorization": "bearer "+token, "User-Agent": user_agent}
    return requests.get("https://oauth.reddit.com/"+url, headers=headers)

def watch_thread(thread):
    most_recent = 0
    while True:
        response = api_request('live/'+thread).json()
        posts = response['data']['children']
        posts.reverse()
        for post in filter(lambda x: x['data']['created_utc'] > most_recent, posts):
            most_recent = post['data']['created_utc']
            body = post['data']['body']
            author = post['data']['author']
            ts = arrow.get(post['data']['created_utc'])
            print('{} {} --{}'.format(ts, body.encode('utf-8'), author.encode('utf-8')))
        time.sleep(5)

if __name__ == '__main__':
    url_path = sys.argv[1] if len(sys.argv) > 1 else 'api/v1/me'
    print(json.dumps(api_request(url_path).json()))

