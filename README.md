# Watch-party

A simple synchronized video player using websockets. 🍿🎦

## Instructions
1. Go to `https://watch-party.app.pxel.pw`.
2. Paste your video file url over HTTP or HTTPS in the input box and click
   `Set URL`.
3. Copy the page URL and send it to your friends!

## Troubleshooting
- Q: Pausing or resuming the video resets the playback position.
- A: Make sure that your video file is served with proper range
  headers. (Try using nginx to serve the files.)

- Q: The video does not play!
- A: Make sure that your video file is accessible by opening the URL
  directly in a new tab. If that works, make sure that the file is
  being served with proper cross-origin headers. This program will not
  work for videos hosted on streaming sites.
