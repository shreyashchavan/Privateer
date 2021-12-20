# Privateer

![Privateer](https://github.com/shreyashchavan/Privateer/blob/main/Privateer.png)

A simple CLI based any Download Tool, that find files and let you stream or download thorugh WebTorrent CLI or Aria or any command tool

## How to use Script:
1. Install Python and PIP

2. Install requirements
```
pip install -r requirements.txt
```
3. Then Download Node JS runtime
[Node js](https://nodejs.org/en/)

4. Install Area2 or webtorrent Cli
```
npm install webtorrent-cli -g
```

## Dependencies:

Install Webtorrent Cli for downloading or Streaming files.

or Install [aria2](https://github.com/aria2/aria2)

#### It supports:
Here is a list of features:
- Command-line interface
- Download files through HTTP(S)/FTP/SFTP/BitTorrent
- Segmented downloading
- Metalink version 4 (RFC 5854) support(HTTP/FTP/SFTP/BitTorrent)
- Metalink version 3.0 support(HTTP/FTP/SFTP/BitTorrent)
- Metalink/HTTP (RFC 6249) support
- HTTP/1.1 implementation
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- Well-known environment variables for proxy: http_proxy, https_proxy, ftp_proxy, all_proxy and no_proxy
- HTTP gzip, deflate content encoding support
- Verify peer using given trusted CA certificate in HTTPS
- Client certificate authentication in HTTPS
-Chunked transfer encoding support
- Load Cookies from file using the Firefox3 format, Chromium/Google Chrome and the Mozilla/Firefox (1.x/2.x)/Netscape format.
- Save Cookies in the Mozilla/Firefox (1.x/2.x)/Netscape format.
- Custom HTTP Header support
- Persistent Connections support
- FTP/SFTP through HTTP Proxy
- Download/Upload speed throttling
- BitTorrent extensions: Fast extension, DHT, PEX, MSE/PSE, Multi-Tracker, UDP tracker
- BitTorrent WEB-Seeding. aria2 requests chunks more than piece size to reduce the request overhead. It also supports pipelined requests with piece size.
- BitTorrent Local Peer Discovery
- Rename/change the directory structure of BitTorrent downloads completely
- JSON-RPC (over HTTP and WebSocket)/XML-RPC interface
- Run as a daemon process
- Selective download in multi-file torrent/Metalink

more features of [aria2](https://github.com/aria2/aria2)

### and Ready to use

![Privateer](https://github.com/shreyashchavan/Privateer/blob/main/Privateer%20-%20Pirate%20Downloader.jpeg)


## Upcomming Update:
- [ ] create Own Scrapper that scrapes
- [ ] Host api on vercel
- [ ] Avoid dependency

### Feel free to Star and PR
Set Upstream to this Url and commit cahnges as below 

*Now you can make changes to the code. The following code creates a new branch, makes an arbitrary change, and pushes it to new_branch:*

1. Once you add all the files in your branch, it time to push your code for generating a pull request.
    ```
    git status
    ```
    > This checks whether you are on your created branch or the master branch. If it shows master, type:
      ```
      git checkout <Your Branch Name>
      ```
      
    Now its time for **the Git operations.** Always **git pull** to ensure that your files are updated.
      ```
      git pull origin master
      ```
      
      ```
      git add .
      ```
      
      ```
      git commit -m "Your Message"
      ```
      
      ```
      git push -u origin <Your Branch Name>
