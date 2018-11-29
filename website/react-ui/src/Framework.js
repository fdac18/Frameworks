import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import Downloads from "./Downloads";
import Overflow from "./Overflow";
import Github from "./Github";
import Wordcloud from "./Wordcloud";
import { frameworks } from "./Constants";

class Framework extends Component {
  constructor(props) {
    super(props);
    const { framework } = this.props.match.params;
    if (!Object.keys(frameworks).includes(framework.toLowerCase())) this.props.history.push("/");

    this.state = {
      framework,
      showDownloads: false,
      showOverflow: false,
      showGithub: false,
      showWordcloud: true
    }
  }

  render() {
    return (
      <div>
        {this.state.showDownloads && <Downloads framework={this.state.framework} />}
        {this.state.showOverflow && <Overflow framework={this.state.framework} />}
        {this.state.showGithub && <Github framework={this.state.framework} />}
        {this.state.showWordcloud && <Wordcloud framework={this.state.framework} />}
      </div>
    )
  }
}

export default withRouter(Framework);
