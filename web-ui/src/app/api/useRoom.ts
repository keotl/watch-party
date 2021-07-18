import { MutableRefObject, useEffect, useRef, useState } from "react";
import {
  pauseMessage,
  playMessage,
  requestResyncMessage,
  setVideoUrlMessage,
} from "./functions";

type RoomState = {
  videoUrl: string;
  setVideoUrl: (url: string) => void;
  pause: (timestamp: number) => void;
  play: (timestamp: number) => void;
  requestResync: () => void;
};

export function useRoom(
  roomName: string,
  onPlay: (timestamp: number) => void,
  onPause: (timestamp: number) => void,
  getCurrentState: () => { isPaused: boolean; currentTime: number }
): RoomState {
  const ws: MutableRefObject<WebSocket | null> = useRef(null);
  useEffect(() => {
    ws.current = new WebSocket("wss://watch-party.app.pxel.pw/ws/" + roomName);
    // ws.current = new WebSocket("ws://localhost:8080/ws/" + roomName);
    ws.current.onopen = () => console.log("ws-opened");
    ws.current.onclose = () => console.log("ws-closed");
    ws.current.onmessage = (e) => {
      console.log(e);
      const message = JSON.parse(e.data);
      switch (message.type) {
        case "SET_URL":
          if (message.url !== videoUrl) {
            setLocalUrl(message.url);
          }
          break;
        case "PLAY":
          onPlay(message.timestamp);
          break;
        case "PAUSE":
          onPause(message.timestamp);
          break;
        case "REQUEST_RESYNC":
          const state = getCurrentState();
          if (state.isPaused) {
            pause(state.currentTime);
          } else {
            play(state.currentTime);
          }
          break;
        default:
          break;
      }
    };
    return () => ws.current!.close();
  }, [roomName]);

  const [videoUrl, setLocalUrl] = useState("");

  function setVideoUrl(url: string) {
    if (ws.current && ws.current.OPEN) {
      ws.current.send(setVideoUrlMessage(url));
      setLocalUrl(url);
    }
  }

    function play(timestamp: number) {
    if (ws.current && ws.current.OPEN) {
      console.log(playMessage(timestamp));
      ws.current.send(playMessage(timestamp));
    }
  }
  function pause(timestamp: number) {
    if (ws.current && ws.current.OPEN) {
      ws.current.send(pauseMessage(timestamp));
    }
  }
  function requestResync() {
    if (ws.current && ws.current.OPEN) {
      ws.current.send(requestResyncMessage());
    }
  }

  return {
    videoUrl,
    setVideoUrl,
    pause,
    play,
    requestResync,
  };
}
