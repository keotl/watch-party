import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { VideoPlayer } from "./app/components/VideoPlayer";

import { createBrowserHistory } from "history";
import { Router } from "react-router-dom";
const history = createBrowserHistory();

function App() {
  if (history.location.pathname === "/") {
    const roomId = Math.round(Math.random() * 1000000000000);
    history.push(`/${roomId}`);
    return <></>;
  }

  return (
    <Router {...{ history }}>
      <div className="App">
        <VideoPlayer />
      </div>
    </Router>
  );
}

export default App;
