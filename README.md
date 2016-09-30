# reddit-api

Python scripts that do stuff with the Reddit API.

## example

```
$ cat ~/.reddit-creds
REDDIT_CREDS=/p-jcoLKBynTLew/gko_LXELoV07ZBNUXrvWZfzE3aI/reddit_bot/snoo
export REDDIT_CREDS
$ source ~/.reddit-creds
$ ./api.py live/xnrdv28vxfi2 | jq .
{
  "kind": "Listing",
  "data": {
    "modhash": null,
    "children": [
      {
        "kind": "LiveUpdate",
        "data": {
          "body": "Elon Musk comparing Mars and Earth - relatively similar temperatures, times, etc., especially after terraforming.",
          "name": "LiveUpdate_45bc84fe-84e5-11e6-87b4-0e83b6d79559",
          "created": 1475031893,
          "embeds": [],
          "author": "Zucal",
          "created_utc": 1475003093,
          "body_html": "&lt;div class=\"md\"&gt;&lt;p&gt;Elon Musk comparing Mars and Earth - relatively similar temperatures, times, etc., especially after terraforming.&lt;/p&gt;\n&lt;/div&gt;",
          "stricken": false,
          "id": "45bc84fe-84e5-11e6-87b4-0e83b6d79559"
        }
      },
      ...

$ ./watch_thread xnrdv28vxfi2
2016-09-27T20:03:57+00:00 https://twitter.com/NASASpaceflight/status/780860452024745985 --Zucal
2016-09-27T20:04:09+00:00 Now moving into Q&amp;A. --Wetmelon
2016-09-27T20:04:58+00:00 Question is about manufacturing site, and prepping the Cape Canaveral launch site. --Zucal
2016-09-27T20:05:13+00:00 https://twitter.com/NASASpaceflight/status/780860701623607296 --Zucal
```

## oauth credentials

Your credentials are passed via the `REDDIT_CREDS` environment variable. This
is simply four credentials, separated by a character of your choice. Clearly,
make sure the separating character does not occur in any of the four
credentials.

The four credentials, in order, are:

1. Application ID
2. Application secret
3. Reddit username
4. Reddit pasword

The first two should be pulled from a "personal use script" that is associated
with your reddit account. See the getting started guide here:

https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example

The last two are your reddit username and password, exactly as you would
expect.

