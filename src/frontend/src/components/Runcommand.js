import React from 'react';
import { Terminal } from 'xterm';
import {
  API_URL
} from '../environment';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

class Runcommand extends React.Component {
  
  constructor() {
    super();
    this.state = {
      command: '',
    };
    this.handleChange = this.handleChange.bind(this);
    console.log(window.location.hostname);
  }

  handleChange({ target }) {
    this.setState({
      [target.name]: target.value
    });
  }

  componentDidMount() {
    var term = new Terminal({
      cursorBlink: true
    });
    term.open(this.terminal);
    const url = 'ws://' + window.location.hostname + API_URL + '/runcommand'
    const socket = new WebSocket(url);
    term.write('$ ');
    let current_line = "";
    let cursor = 0;
  	term.onKey((data) => {
      switch(data.domEvent.key) {
        case "Enter":
          term.write("\r\n");
          if(current_line) {
            socket.send(JSON.stringify({
              command: current_line
            }));
          } else {
            term.write("\r\n");
            term.write("$ ");
          }
          cursor = 0;
          current_line = "";
          break;
        default:
          if (cursor < 120) {
            cursor += 1;
            current_line += data.key;
            term.write(data.key);
          }
          break;
      }
    });
  }

  render() {
    return (
      <>
        <div>
          <div style={{padding:'10px'}}>
            <div ref={ref=>this.terminal = ref}></div>
          </div>
        </div>
      </>
    );
  };
};

export default Runcommand;
