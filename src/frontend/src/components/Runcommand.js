import React from 'react';
import { Card, Col, Container, Row, Form, Button } from 'react-bootstrap';
import Console from './Console';

class Runcommand extends React.Component {

  handleSubmit(event){
    console.log('hello');
    console.log(event);
  }
  
  render() {
    return (
      <>
        <Container>
          <Row>
            <Col>
              <Card className="text-left">
                <Card.Header>
                  <h3>Terminal</h3>
                </Card.Header>
                <Card.Body>
                  <Console />
                </Card.Body>
              </Card>
            </Col>
          </Row>
          <Row>
            <Card className="text-left">
              <Card.Header>
                <h3>File Upload</h3>
              </Card.Header>
              <Card.Body>
                <h5>This file will upload to '/tmp'.</h5>
                <input type="file" onClick={this.handleSubmit}/><br/><br/>
                <Button variant="dark">Upload</Button>
              </Card.Body>
            </Card>
          </Row>
        </Container>
      </>
    );
  };
};

export default Runcommand;
