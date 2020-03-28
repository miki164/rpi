import React, {Component} from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useParams
} from "react-router-dom";
import * as qs from 'qs';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = { apiResponse: "" };
    }

    callAPI() {
        fetch("http://localhost:9000/API/")
            .then(res => res.text())
            .then(res => this.setState({ apiResponse: res}))
            .catch(err => err);
    }

    componentDidMount() {
        this.callAPI();
    }

    render() {
        return (
            <Router>
                <div>
                    <Switch>
                        <Route path="/">
                           <div dangerouslySetInnerHTML={{ __html: this.state.apiResponse }} />
                        </Route>
                    </Switch>
                </div>
            </Router>
        )
    }
}

export default App;
