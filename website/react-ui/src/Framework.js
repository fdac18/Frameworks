import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import { CanvasJSChart } from "./lib/canvasjs.react";

const frameworks = {
  "angular": {
    proper: "Angular"
  }, "react": {
    proper: "React"
  }, "backbone": {
    proper: "Backbone.js"
  }, "ember": {
    proper: "Ember.js"
  }, "jquery": {
    proper: "jQuery"
  }, "vue": {
    proper: "Vue.js"
  }
};

class Framework extends Component {
  constructor(props) {
    super(props);
    const { framework } = this.props.match.params;
    if (!Object.keys(frameworks).includes(framework.toLowerCase())) this.props.history.push("/");

    this.state = {
      downloads: require(`./data/${framework}_downloads.json`)
    }
  }

  render() {
    const { framework } = this.props.match.params;
    const { downloads } = this.state;
    const dataPoints = downloads.map(day => {
      const date = day.d.split('-');
      return {
        x: new Date(date[0], parseInt(date[1]) - 1, date[2]),
        y: day.c
      }
    });
    const options = {
      theme: "light2",
      animationEnabled: true,
      zoomEnabled: true,
      title: {
        text: `${frameworks[framework.toLowerCase()].proper} Downloads`
      },
      axisY: {
        title: "Downloads",
        includeZero: false
      },
      axisX: {
        labelAngle: -30
      },
      data: [{ type: "area", dataPoints }]
    }
    return (
      <CanvasJSChart options={options} />
    );
  }
}

export default withRouter(Framework);
