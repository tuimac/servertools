import React from 'react';
import {
  Nav,
  Navbar,
  Card
} from 'react-bootstrap';

class EC2 extends React.Component {

  constructor() {
    super();
    this.state = {
      result: {}
    };
  }

  componentDidMount() {
    const url = window.location.origin + '/api/ec2'
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          console.log(url);
          console.log(result);
          this.setState({
            result: result,
          });
        },
        (error) => {
          this.setState({
            result: error
          });
        }
      )
  }

  render() {
    const { results } = this.state;
    return(
      <>
      </>
    );
  };
}

export default EC2;
