import React, { Component } from "react";
import { CanvasJSChart } from "./lib/canvasjs.react";
import { frameworks } from "./Constants";
import "./Frameworks.css";

class Downloads extends Component {
  constructor(props) {
    super(props);

    const { framework } = props;

    this.state = {
      framework,
      downloads: require(`./data/${framework}_downloads.json`)
    }
  }

  render() {
    const { framework, downloads } = this.state;
    const dataPoints = downloads.map(day => {
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
        text: `${frameworks[framework.toLowerCase()].proper} Downloads`
      },
      axisY: {
        title: "Downloads",
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

export default Downloads;