#!/usr/bin/env python

import requests
import os
import sys
import json
import arrow

def unpack_creds():
    env_var = os.environ['REDDIT_CREDS']
    sep_char = env_var[0]
    return env_var[1:].split(sep_char)

def api_request(url):
    user_agent = "reddit-api/0.1"
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

def live_thread_post(post, action='print'):
    if action == 'print':
        body = post['body'].strip()
        author = post['author']
        ts = arrow.get(post['created_utc']).to('local').format('h:mma')
        print('{} {}\n{}\n'.format(ts, author.encode('utf-8'), body.encode('utf-8')))
    else:
        pass

if __name__ == '__main__':
    url_path = sys.argv[1] if len(sys.argv) > 1 else 'api/v1/me'
    print(json.dumps(api_request(url_path).json()))
