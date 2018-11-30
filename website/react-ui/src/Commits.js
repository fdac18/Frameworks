import React, { Component } from "react";
import { CanvasJSChart } from "./lib/canvasjs.react";
import { frameworks } from "./Constants";

class Github extends Component {
  constructor(props) {
    super(props);

    const { framework } = props;

    this.state = {
      framework,
      commits: require(`./data/${framework}_commits.json`)
    }
  }

  render() {
    const { framework, commits } = this.state;
    const dataPoints = commits.map(day => {
      const date = day.d.split('-');
      return {
        x: new Date(date[0], parseInt(date[1], 10) - 1, date[2]),
        y: day.c
      }
    });
    const options = {
      theme: "light2",
      animationEnabled: true,
      zoomEnabled: true,
      title: {
        text: `${frameworks[framework.toLowerCase()].proper} Commits`
      },
      axisY: {
        title: "Commits",
        includeZero: false
      },
      axisX: {
        labelAngle: -30
      },
      data: [{ type: "area", dataPoints }],
      height: this.props.height
    }
    return (
      <CanvasJSChart options={options} />
    );
  }
}

export default Github;