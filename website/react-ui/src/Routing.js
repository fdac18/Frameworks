import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from "./Header.js";
import Homepage from "./Homepage.js";
import Framework from "./Framework.js";
import Footer from "./Footer.js";
import "./Frameworks.css";

class Routing extends Component {
  render() {
    return (
      <Router>
        <div className="Homepage">
          <Header />
          <Switch>
            <Route exact path="/" component={Homepage} />
            <Route exact path="/:framework" component={Framework} />
            <Route component={Homepage} />
          </Switch>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default Routing;
