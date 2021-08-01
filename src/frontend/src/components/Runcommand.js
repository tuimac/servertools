import React from 'react';
import { API_URL } from '../environment';
import { Card, Nav } from 'react-bootstrap';
import Console from './Console';

class Runcommand extends React.Component {
  
  render() {
    return (
      <>
        <Nav variant="tabs">
          <Nav.Item>
            <Nav.Link>Console 1</Nav.Link>
            <Card className="text-center">
              <Card.Body>
                <Console />
              </Card.Body>
            </Card>
          </Nav.Item>
        </Nav>
      </>
    );
  };
};

export default Runcommand;
