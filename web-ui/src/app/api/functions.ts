export function setVideoUrlMessage(url: string) {
  return JSON.stringify({
    type: "SET_URL",
    url,
  });
}

export function pauseMessage(timestamp: number) {
  return JSON.stringify({
    type: "PAUSE",
    timestamp,
  });
}

export function playMessage(timestamp: number) {
  return JSON.stringify({
    type: "PLAY",
    timestamp,
  });
}

export function requestResyncMessage() {
  return JSON.stringify({
    type: "REQUEST_RESYNC",
  });
}
