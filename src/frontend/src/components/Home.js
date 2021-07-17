import React from 'react';
import {
  Nav,
  Navbar,
} from 'react-bootstrap';
import SideBar from './SideBar';

class Home extends React.Component {

  constructor() {
    super();
    this.state = {
      name: ''
    };
  }

  render() {
    return(
      <>
        <div>
          <SideBar></SideBar>
        </div>
        <div>
          <Navbar bg="primary" variant="dark">
            <Navbar.Brand href="/">Server Tools</Navbar.Brand>
            <Nav className="mr-auto">
              <Nav.Link href="/runcommand">Runcommad</Nav.Link>
            </Nav>
          </Navbar>
        </div>
      </>
    );
  };
}

export default Home;
