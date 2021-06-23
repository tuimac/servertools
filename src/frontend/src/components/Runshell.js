import React from 'react';
import { Redirect } from 'react-router-dom';

class Runshell extends React.Component {
  
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

  componentDidMount() {
    console.log(window.location.hostname);
  }

  render() {
    return (
      <>
        <div>
          <Redirect to='/api/runshell' />
        </div>
      </>
    );
  };
};

export default Runshell;
