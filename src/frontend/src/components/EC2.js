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
    const url = window.location.origin + process.env.BACKEND_URL + '/ec2'
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            result: result,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    return(
      <>
        <div>
          <Card style={{ width: '25rem' }} className="text-center">
            <Card.Header>
              <h1>AWS Information</h1>
            </Card.Header>
            <Card.Body>
              
            </Card.Body>
          </Card>          
        </div>
      </>
    );
  };
}

export default EC2;
