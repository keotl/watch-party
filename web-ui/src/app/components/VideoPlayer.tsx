import { useRef, useState } from "react";
import { useLocation } from "react-router-dom";
import { useRoom } from "../api/useRoom";
import styles from "./VideoPlayer.module.css";

export function VideoPlayer() {
  const { pathname } = useLocation();
  const [formUrl, setFormUrl] = useState("");
  const videoElement = useRef<HTMLVideoElement>(null);

  function onPlay(timestamp: number) {
    if (videoElement.current) {
      videoElement.current.currentTime = timestamp;
      if (videoElement.current.paused) {
        videoElement.current.play();
      }
    }
  }

  function onPause(timestamp: number) {
    if (videoElement.current) {
      videoElement.current.currentTime = timestamp;
      if (!videoElement.current.paused) {
        videoElement.current.pause();
      }
    }
  }

  function getCurrentState() {
    if (videoElement.current) {
      return {
        isPaused: videoElement.current.paused,
        currentTime: videoElement.current.currentTime,
      };
    }
    return { isPaused: true, currentTime: 0 };
  }

  const room = useRoom(pathname, onPlay, onPause, getCurrentState);

  return (
    <div className={styles.container}>
      <div className={styles.videoPanel}>
          <video
      className={styles.video}
          ref={videoElement}
          src={room.videoUrl}
      height="100%"
      width="100%"
          onPlayCapture={(e) => room.play(e.currentTarget.currentTime)}
          onPauseCapture={(e) => room.pause(e.currentTarget.currentTime)}
          controls
          muted
        ></video>
      </div>
	  <div className={styles.optionsPanel}>
	  <h1>Watch Party
	  </h1>
        <input
          type="text"
          name="video-url"
          value={formUrl}
          onChange={(e) => setFormUrl(e.target.value)}
        />
        <button onClick={() => room.setVideoUrl(formUrl)}>Set URL</button>
      </div>
    </div>
  );
}
