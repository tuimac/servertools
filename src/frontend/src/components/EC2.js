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
    const result = this.state.result.InstanceIDDocument;
    console.log(result);
    const table = [];

    table.push(<Table striped bordered hover variant="dark" responsive="sm" responsive="md" responsive="lg" responsive="xl"><tbody>);
    {
      Object.keys(result).map(key =>
        <tr><td>{key}</td><td>{result[key]}</td></tr>
      )
    }
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
