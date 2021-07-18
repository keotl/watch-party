# Watch-party

A synchronized video player using websockets. 🍿🎦


## Troubleshooting
- Q: Pausing or resuming the video resets the playback position.
- A: Make sure that your video file is served with proper range
  headers. (Try using nginx to serve the files.)

- Q: The video does not play!
- A: Make sure that your video file is accessible by opening the URL
  directly in a new tab. If that works, make sure that the file is
  being served with proper cross-origin headers. This program will not
  work for videos hosted on streaming sites.
