import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import './App.css';
import Landing from '../landing/Landing';
import Channel from '../channel/channel';

const App = () => {
  return (
    <div className="app-container">
      <Router>
        <Switch>
          <Route exact path="/" component={Landing} />
          <Route exact path="/channel/:channelId" component={Channel} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
