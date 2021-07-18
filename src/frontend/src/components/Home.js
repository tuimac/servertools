import React from 'react';
import {
  Nav,
  Navbar,
  Card
} from 'react-bootstrap';

class Home extends React.Component {

  constructor() {
    super();
    this.state = {
      result: {}
    };
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

export default Home;
