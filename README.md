# reddit-live-cli

This is a python script that does stuff with the Reddit API.

## example

```
$ cat ~/.reddit-live-cli-creds
REDDIT_LIVE_CREDS=/p-jcoLKBynTLew/p-jcoLKBynTLew/reddit_bot/snoo
export REDDIT_LIVE_CREDS
$ source ~/.reddit-live-cli-creds
$ get-url live/xnrdv28vxfi2 | jq .
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
```

## oauth credentials

Your credentials are passed via the `REDDIT_LIVE_CREDS` environment
variable. This is simply four credentials, separated by a character of
your choice. Clearly, make sure the separating character does not occur
in any of the four credentials.

The four credentials, in order, are:

1. Application ID
2. Application secret
3. Reddit username
4. Reddit pasword

The first two should be pulled from a "personal use script" that is
associated with your reddit account. See the getting started guide here:

https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example

