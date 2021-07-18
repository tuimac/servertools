import React from 'react';
import './App.css';
import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Home from './components/Home';
import Runcommand from './components/Runcommand';
import Layout from './components/Layout';

class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
    };

    this.previousWidth = -1;
  }

  updateWidth() {
    const width = window.innerWidth;
    const widthLimit = 576;
    this.previousWidth = width;
  }

  componentDidMount() {
    this.updateWidth();
    window.addEventListener("resize", this.updateWidth.bind(this));
  }

  componentWillUnmount() {
    window.removeEventListener("resize", this.updateWidth.bind(this));
  }

  toggle = () => {
    this.setState({ isOpen: !this.state.isOpen });
  };

  render() {
    return (
			<>
        <BrowserRouter>
          <div>
            <Layout toggle={this.toggle} isOpen={this.state.isOpen} />
            <div>
              <Switch>
                <Route exact path="/">
                  <Redirect to="/home" />
                </Route>
                <Route component={ Home } path="/home" exact />
                <Route component={ Runcommand } path="/runcommand" exact />
              </Switch>
            </div>
          </div>
        </BrowserRouter>
      </>
    );
  }
}

export default App;
