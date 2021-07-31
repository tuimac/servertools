import React from 'react';
import {
  Nav,
  Navbar,
  Button,
  Container,
  Row,
  Col
} from 'react-bootstrap';
import { Link } from "react-router-dom";
import classNames from "classnames";

class Layout extends React.Component {

  render() {
    return(
      <div>
        <Navbar bg="primary" variant="light">
          <Navbar.Brand href="/">Server Tools</Navbar.Brand>
          <Nav variant="pills">
            <Nav.Item>
              <Nav.Link href="/">Home</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/runcommand">Runcommmand</Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar>
      </div>
    );
  };
}

export default Layout;
