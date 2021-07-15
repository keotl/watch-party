import React from 'react';
import logo from './logo.svg';
import './App.css';
import { VideoPlayer } from './app/components/VideoPlayer';

import {createBrowserHistory} from 'history';
import { Router } from 'react-router-dom';
const history = createBrowserHistory();

function App() {
    return (
	<Router {...{history}} >
    <div className="App">
	  <VideoPlayer />
	    </div>
	    </Router>
  );
}

export default App;
