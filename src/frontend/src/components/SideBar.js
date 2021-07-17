import React from 'react';
import {
  Nav,
  Navbar,
} from 'react-bootstrap';
import { Link } from "react-router-dom";

class SideBar extends React.Component {

  constructor() {
    super();
    this.state = {
      name: ''
    };
  }

  render() {
    return(
      <div>
        <ul class="list-unstyled components">
          <p>Dummy Heading</p>
          <li class="active">
            <ul class="collapse list-unstyled" id="homeSubmenu">
              <li>
                <Link to="/">Home</Link>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    );
  };
}

export default SideBar;
