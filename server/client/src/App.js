import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = { apiResponse: "" };
    }

    callAPI() {
        fetch("http://localhost:9000/API/")
            .then(res => res.text())
            .then(res => console.log(res))
            .catch(err => err);
    }

    componentDidMount() {
        this.callAPI();
        console.log(this.state.apiResponse)
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <h1 className="App-title">Hi</h1>
                </header>
                <p className="App-intro">{this.state.apiResponse}</p>
            </div>
        )
    }
}
export default App;
