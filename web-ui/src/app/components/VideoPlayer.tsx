import { useEffect, useRef, useState } from "react";
import { useLocation } from "react-router-dom";

export function VideoPlayer() {
  const [url, setUrl] = useState("");
  const { pathname } = useLocation();
  const ws = useRef(new WebSocket("ws://watch-party.app.pxel.pw/ws"));

  useEffect(() => {
    ws.current = new WebSocket("wss://watch-party.app.pxel.pw/ws" + pathname);
    ws.current.onopen = () => console.log("ws-opened");
    ws.current.onclose = () => console.log("ws-closed");
      ws.current.onmessage = e => console.log(e);
    return () => ws.current.close();
  }, [pathname]);

  return (
    <div>
      <video src={url} controls></video>
    </div>
  );
}
