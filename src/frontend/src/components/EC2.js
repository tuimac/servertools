import React from 'react';
import {
  Nav,
  Navbar,
  Card,
  Spinner,
  Table
} from 'react-bootstrap';

class EC2 extends React.Component {

  constructor() {
    super();
    this.state = {
      result: null
    };
  }

  componentDidMount() {
    const url = window.location.origin + '/api/ec2';
    fetch(url).then(res => res.json()).then(
      (result) => {
        this.setState({
          result: result,
        });
      },
      (error) => {
        this.setState({
          result: error
        });
      }
    );
  }

  createTable() {
    const result = this.state.result;
    console.log(result);
    const table = [];

    table.push(<Table striped bordered hover variant="dark"><tbody>);
    table.push(</tbody></Table>);

    return table;
  }

  render() {
    if(this.state.result == null) {
      return(
        <Spinner animation="border" role="status">
          <span className="sr-only"></span>
        </Spinner>
      )
    } else {
      return(
        <>
          { this.createTable() }
        </>
      )
    }
  };
}

export default EC2;
