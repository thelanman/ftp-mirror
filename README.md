# FTP-Buckup

This utility was born out of the need to automatically backup files off a mobile device via FTP. While initially researching the problem, I found many apps that backedup mobile files to third party services such as Google Drive, OneDrive, Dropbox, etc. but none that would backup to a a sharedrive or FTP server running on the home LAN. I also did not want to be bothered by using a USB to connect mobile device to PC and navigate files and do this process by hand.

Enter [ES File Explorer](https://play.google.com/store/apps/details?id=com.estrongs.android.pop&hl=en). This app is by far the best mobile file manager. One of the cooler features is that it allows you to turn your phone into a mobile FTP server. So now with one tap of the button on the phone to turn on the server and one command to run this script on the PC, I can sync all specified files to my main home storage!

Of course, this will work with any FTP server too :)

### Requirements
-Python 2.7+

### Usage
```sh
$ python mirror.py -h 
usage: mirror.py [-h] [--port POT] ip src_path dst_path

Sync a remote FTP server to local storage

positional arguments:
  ip           IPv4 address of remote FTP server
  src_path     source path on remote FTP server
  dst_path     local path to save remotely downloaded files
```
optional arguments:
  -h, --help   show this help message and exit
  --port PORT  port number of remote FTP server (default=21)
### Version
1.0.0

### Todos

 - Do logging
 - Handle errors
 - Compare file attributes instead of just name
 - Add options for handling duplicate filenames

### License
MIT
