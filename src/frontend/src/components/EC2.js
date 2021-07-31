import React from 'react';
import {
  Nav,
  Navbar,
  Card,
  Spinner,
  ListGroup
} from 'react-bootstrap';

class EC2 extends React.Component {

  constructor() {
    super();
    this.state = {
      result: null
    };
  }

  componentDidMount() {
    const url = window.location.origin + '/api/ec2'
    fetch(url).then(res => res.json()).then(
      (result) => {
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
    if(this.state.result == null) {
      return(
        <Spinner animation="border" role="status">
          <span className="sr-only"></span>
        </Spinner>
      )
    } else {
      console.log(this.state);
      const result = this.state.result;
      for(let key in result) {
        return(
          <>
            {key} {resuls[key]}
          </>
        );
      }
    }
  };
}

export default EC2;
