import React from 'react';
import './App.css';
import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Home from './components/Home';
import Runcommand from './components/Runcommand';
import Runshell from './components/Runshell';

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Redirect to="/home" />
          </Route>
          <Route component={ Home } path="/home" exact />
          <Route component={ Runcommand } path="/runcommand" exact />
          <Route component={ Runshell } path="/runshell" exact />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
