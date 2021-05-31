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
      cursorBlink: true,
      cursorStyle: 'block',
      scrollback: 100
    });
    term.open(this.terminal);
    const url = 'ws://' + window.location.hostname + API_URL + '/runcommand'
    const socket = new WebSocket(url);
    socket.addEventListener('message', (response) => {
      response = JSON.parse(response.data).result
      if(response === false) {
        term.write('\r\n' + '$ ');
      } else {
        term.write(response + '\r\n');
      }
    });
    term.write('$ ');
    let currentInput = '';
    let inputHistory = [];
    let cursor = 0;
    let historyIndex = 0;
  	term.onKey((data) => {
      console.log(data.domEvent.key); 
      switch(data.domEvent.key) {
        case 'Enter':
          term.write('\r\n');
          if(currentInput) {
            socket.send(JSON.stringify({
              command: currentInput
            }));
          } else {
            term.write('\r\n');
            term.write('$ ');
          }
          cursor = 0;
          historyIndex++;
          inputHistory.push(currentInput);
          currentInput = '';
          break;
        case 'Backspace':
          currentInput = currentInput.substring(0, currentInput.length - 1);
          console.log(currentInput);
          term.write(currentInput);
        case 'ArrowUp':
          if(historyIndex >= 0) {
            historyIndex--;
            currentInput = inputHistory[historyIndex];
            term.write(currentInput);
          }
        default:
          if (cursor < 120) {
            cursor += 1;
            currentInput += data.key;
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
          <div style={{ padding:'10px' }}>
            <div ref={ ref=>this.terminal = ref }></div>
          </div>
        </div>
      </>
    );
  };
};

export default Runcommand;
