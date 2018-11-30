import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import Downloads from "./Downloads";
import Overflow from "./Overflow";
import Commits from "./Commits";
import Wordcloud from "./Wordcloud";
import Issues from "./Issues";
import { frameworks } from "./Constants";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import { withStyles } from "@material-ui/core/styles";

const styles = theme => ({
  root: {
    flexGrow: 1,
    width: '100%',
    backgroundColor: theme.palette.background.paper,
  }
});

class Framework extends Component {
  constructor(props) {
    super(props);
    const { framework } = this.props.match.params;
    if (!Object.keys(frameworks).includes(framework.toLowerCase())) this.props.history.push("/");

    const width = Math.max(document.body.clientWidth, window.innerWidth || 0)
    const smallScreen = width < 600;

    this.state = {
      framework,
      top: 0,
      bottom: 0,
      scrollable: smallScreen,
      cenetered: !smallScreen,
      height: ((Math.max(document.body.clientHeight, window.innerHeight || 0) - 90 - 50 - 96) / 2),
      width
    }
  }

  updateDimensions = () => {
    const width = Math.max(document.body.clientWidth, window.innerWidth || 0);
    const height = Math.max(document.body.clientHeight, window.innerHeight || 0);
    this.setState({ height: ((height - 90 - 50 - 96) / 2), width });
  }

  componentDidMount() {
    this.updateDimensions();
    window.addEventListener("resize", this.updateDimensions)
  }

  componentWillUnmount() {
    window.removeEventListener("resize", this.updateDimensions)
  }

  render() {
    const { framework } = this.props.match.params;
    if (!Object.keys(frameworks).includes(framework.toLowerCase())) return null;
    const { classes } = this.props;
    const { top, bottom, scrollable, centered, height, width } = this.state;
    return (
      <div className={classes.root}>
        <AppBar position="static" color="default">
          <Tabs
            value={top}
            onChange={(e, top) => this.setState({ top })}
            indicatorColor="primary"
            textColor="primary"
            scrollable={scrollable}
            scrollButtons="auto"
            centered={centered}
          >
            <Tab label="Downloads" />
            <Tab label="Tag cloud" />
            <Tab label="Overflow" />
            <Tab label="Commits" />
            <Tab label="Issues" />
          </Tabs>
        </AppBar>
        {top === 0 && <Downloads framework={this.state.framework} height={height} />}
        {top === 1 && <Wordcloud framework={this.state.framework} height={height} width={width} />}
        {top === 2 && <Overflow framework={this.state.framework} height={height} />}
        {top === 3 && <Commits framework={this.state.framework} height={height} />}
        {top === 4 && <Issues framework={this.state.framework} height={height} />}
        {bottom === 0 && <Downloads framework={this.state.framework} height={height} />}
        {bottom === 1 && <Wordcloud framework={this.state.framework} height={height} width={width} />}
        {bottom === 2 && <Overflow framework={this.state.framework} height={height} />}
        {bottom === 3 && <Commits framework={this.state.framework} height={height} />}
        {bottom === 4 && <Issues framework={this.state.framework} height={height} />}
        <AppBar position="static" color="default">
          <Tabs
            value={bottom}
            onChange={(e, bottom) => this.setState({ bottom })}
            indicatorColor="primary"
            textColor="primary"
            scrollable={scrollable}
            scrollButtons={scrollable ? "auto" : null}
            centered={centered}
          >
            <Tab label="Downloads" />
            <Tab label="Tag cloud" />
            <Tab label="Overflow" />
            <Tab label="Commits" />
            <Tab label="Issues" />
          </Tabs>
        </AppBar>
      </div>
    )
  }
}

export default withRouter(withStyles(styles)(Framework));
