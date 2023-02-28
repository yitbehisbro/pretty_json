# pretty_json
Reformats the json file as well as a fetches from URL.

# Supports:
- Linux
- macOS

# Installation
- Clone the repo to your local machine:
<pre><code> git clone https://github.com/yitbehisbro/pretty_json.git </code></pre>
- Change directory to <code>pretty_json</code>:
<pre><code> cd pretty_json</code></pre>
- Change the mode of file to executable:
<pre><code> chmod u+x *</code></pre>
- Execute the <code>INSTALL</code> file:
<pre><code>./INSTALL</code></pre>

# Usage
Usage:    
<pre><code>pretty [filename ... [filename ... [filename ...] ] ]</code></pre>
Example:    
<pre><code><b>yitbe@ubuntu:~$</b> pretty abc.json cde.json fgh.json

Please wait...
Will be created at "reformated/abc.json"
Done.
--
Will be created at "reformated/cde.json"
Done.
--
Will be created at "reformated/fgh.json"
Done.
--
<b>yitbe@ubuntu:~$</b>
</code></pre>
Usage:
<pre><code><b>yitbe@ubuntu:~$</b> pretty *.json </code></pre>
Usage:
<pre><code>pretty URL </code></pre>
Example:
<pre><code>
<b>yitbe@ubuntu:~$</b> curl https://www.reddit.com/r/python/hot.json
{"kind": "Listing", "data": {"after": "t3_11dpfze", "dist": 27, "modhash": "", "geo_filter": null, "children": [{"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "Python", "selftext": "Tell /r/python what you're working on this week! You can be bragging, grousing, sharing your passion, or explaining your pain. Talk about your current project or your pet project; whatever you want to share.", "author_fullname": "t2_145f96", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "Sunday Daily Thread: What's everyone working on this week?", "link_flair_richtext": [{"e": "text", "t": "Daily Thread"}], "subreddit_name_prefixed": "r/Python", ...
<b>yitbe@ubuntu:~$</b>
<b>yitbe@ubuntu:~$</b> curl https://jsonplaceholder.typicode.com/users/1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}<b>yitbe@ubuntu:~$</b>
<b>yitbe@ubuntu:~$</b> pretty https://www.reddit.com/r/python/hot.json https://jsonplaceholder.typicode.com/users/1

Please wait...

Done.
Created at "url_to_json/2023-02-28-15-03-45.json"

Done.
Created at "url_to_json/2023-02-28-15-03-57.json"

Some files might not be reformated.
Please refer /home/user/reformated/ or
/home/user/url_to_json/ for more.
<b>yitbe@ubuntu:~$</b>
<b>yitbe@ubuntu:~$</b> less url_to_json/2023-02-28-15-03-57.json

{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
url_to_json/2023-02-28-15-03-57.json (END)

<b>yitbe@ubuntu:~$</b>
<b>yitbe@ubuntu:~$</b> less url_to_json/2023-02-28-15-03-45.json

{
  "kind": "Listing",
  "data": {
    "after": "t3_11dza2n",
    "dist": 27,
    "modhash": "",
    "geo_filter": null,
    "children": [
      {
        "kind": "t3",
        "data": {
          "approved_at_utc": null,
          "subreddit": "Python",
          "selftext": "Tell /r/python what you're working on this week! You can be bragging, grousing, sharing your passion, or explaining your pain. Talk about your current project or your pet project; whatever you want to share.",
          "author_fullname": "t2_145f96",
          "saved": false,
          "mod_reason_title": null,
          "gilded": 0,
          "clicked": false,
          "title": "Sunday Daily Thread: What's everyone working on this week?",
          "link_flair_richtext": [
            {
              "e": "text",
              "t": "Daily Thread"
            }
          ],
          "subreddit_name_prefixed": "r/Python",
          "hidden": false,
          "pwls": 6,
          "link_flair_css_class": "daily-thread",
          "downs": 0,
          "thumbnail_height": null,
          "top_awarded_type": null,
          "hide_score": false,
          "name": "t3_11bzuxb",
          "quarantine": false,
          "link_flair_text_color": "light",
          "upvote_ratio": 1.0,
          "author_flair_background_color": "#7289da",
          "subreddit_type": "public",
          "ups": 3,
          "total_awards_received": 0,
url_to_json/2023-02-28-15-03-45.json
</code></pre>
# Output
The reformated json file will be saved on the directory <pre><code>$PWD/reformated/</code></pre>
Fetches from URL will be saved in <pre><code>$PWD/url_to_json/</code></pre>
