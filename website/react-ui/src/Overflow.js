import React, { Component } from "react";
import { CanvasJSChart } from "./lib/canvasjs.react";
import { frameworks } from "./Constants.js";

class Overflow extends Component {
  constructor(props) {
    super(props);

    const { framework } = props.framework;

    this.state = {
      framework,
      overflow: require(`./data/${framework}_overflow.json`)
    }
  }

  render() {
    const { framework, overflow } = this.state;
    const dataPoints = overflow.map(day => {
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
        text: `${frameworks[framework.toLowerCase()].proper} Stack Overflow Posts`
      },
      axisY: {
        title: "Stack Overflow Posts",
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

export default Overflow;