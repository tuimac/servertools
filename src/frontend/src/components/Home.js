import React from 'react';
import {
  Card,
  Container,
  Row,
  Col
} from 'react-bootstrap';
import EC2 from './EC2';

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
        <Container>
          <Row>
            <Col>
              <Card className="text-center">
                <Card.Header>
                  <h1>AWS Information</h1>
                </Card.Header>
                <Card.Body>
                  <EC2 />
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </>
    );
  };
}

export default Home;
