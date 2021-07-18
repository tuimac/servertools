import React from 'react';
import {
  Nav,
  Navbar,
  Button,
  Offcanvas
} from 'react-bootstrap';
import { Link } from "react-router-dom";

class Layout extends React.Component {

  constructor() {
    super();
    this.state = {
      open: false
    };
  }



  render() {
    const [show, setShow] = useState(false)
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return(
      <div>
        <Navbar bg="primary" variant="dark">
          <Button variant="primary" onClick={ handleShow }></Button>
          <Navbar.Brand href="/">Server Tools</Navbar.Brand>
        </Navbar>
        <Offcanvas show={ show } onHide={ handleClose }>
          <Offcanvas.Body>
            <Nav defaultActiveKey="/home" className="flex-column">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="/runcommand">Runcommand</Nav.Link>
            </Nav>
          </Offcanvas.Body>
        </Offcanvas>
      </div>
    );
  };
}

export default Layout;
