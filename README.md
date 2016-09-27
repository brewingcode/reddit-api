# reddit-live-cli

This is a python script that does stuff with the Reddit API
See the example here:

https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example

## example

```
$ get-url live/xnrdv28vxfi2
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

