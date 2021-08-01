import React from 'react';
import { Card, Col, Container, Row, Form, Button } from 'react-bootstrap';
import Console from './Console';

class Runcommand extends React.Component {

  handleSubmit = (event) => {
    console.log('hello');
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
                <Form onSubmit={this.handleSubmit}>
                  <Form.Group>
                    <Form.Label><h5>This file will upload to '/tmp'</h5></Form.Label>
                    <Form.File /><br />
                    <Button variant="dark" type="submit">Upload</Button>
                  </Form.Group>
                </Form>
              </Card.Body>
            </Card>
          </Row>
        </Container>
      </>
    );
  };
};

export default Runcommand;
