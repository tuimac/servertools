import React from 'react';
import {
  Nav,
  Navbar,
} from 'react-bootstrap';
import { Link } from "react-router-dom";

class Layout extends React.Component {

  constructor() {
    super();
    this.state = {
      name: ''
    };
  }

  render() {
    return(
      <div>
        <Navbar bg="primary" variant="dark">
          <Navbar.Brand href="/">Server Tools</Navbar.Brand>
          <Nav className="mr-auto">
            <Nav.Link href="/runcommand">Runcommad</Nav.Link>
          </Nav>
        </Navbar>
        <ul class="list-unstyled components">
          <p>Dummy Heading</p>
          <li class="active">
            <a href="/">Home</a>
            <ul class="collapse list-unstyled" id="homeSubmenu">
              <li>
                <Link to="/">Home</Link>
              </li>
            </ul>
          </li>
          <li>
            <a href="/runcommand">Runcommand</a>
          </li>
        </ul>
      </div>
    );
  };
}

export default Layout;
