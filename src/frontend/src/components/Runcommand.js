import React from 'react';
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
  }

  handleChange({ target }) {
    this.setState({
      [target.name]: target.value
    });
  }

  render() {
    return (
      <>
        <div>
          Runcommand
          { API_URL }
        </div>
      </>
    );
  };
};

export default Runcommand;
