import React from 'react';
import { Terminal } from 'xterm';
import { API_URL } from '../environment';

class Runcommand extends React.Component {
  
  constructor() {
    super();
  }

  componentDidMount() {
    const url = 'ws://' + window.location.hostname + API_URL + '/runcommand'
    const socket = new WebSocket(url);
    let currentInput = '';
    let inputHistory = [];
    let cursor = 0;
    let historyIndex = 0;

    var term = new Terminal();
    term.setOption('theme', {
      background: '#202B33',
      foreground: '#F5F8FA'
    })
    term.open(this.terminal);
    term.write('$ ');
    socket.addEventListener('message', (response) => {
      response = JSON.parse(response.data).result
      if(response === false) {
        term.write('\r\n' + '$ ');
      } else {
        term.write(response + '\r\n');
      }
    });

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
          historyIndex++;
          inputHistory.push(currentInput);
          currentInput = '';
          break;
        case 'Backspace':
          currentInput = currentInput.substring(0, currentInput.length - 1);
          console.log(currentInput);
          term.write('\b \b');
          break;
        case 'ArrowUp':
          if(historyIndex > 0) {
            historyIndex--;
            currentInput = inputHistory[historyIndex];
            term.write('');
            term.write('\r');
            term.write('$ ')
            term.write(currentInput);
          }
          break;
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
        <div ref={ id => this.terminal = id }></div>
      </>
    );
  };
};

export default Runcommand;
