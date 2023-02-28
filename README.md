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
<pre><code><b>yitbe@ubuntu:~$</b> pretty https://www.reddit.com/r/python/hot.json https://jsonplaceholder.typicode.com/users/1

Please wait...

Done.
Created at "url_to_json/2023-02-28-15-03-45.json"

Done.
Created at "url_to_json/2023-02-28-15-03-57.json"

Some files might not be reformated.
Please refer /home/user/reformated/ or
/home/user/url_to_json/ for more.
<b>yitbe@ubuntu:~$</b>
</code></pre>
# Output
The reformated json file will be saved on the directory <pre><code>$PWD/reformated/</code></pre>
Fetches from URL will be saved in <pre><code>$PWD/url_to_json/</code></pre>
