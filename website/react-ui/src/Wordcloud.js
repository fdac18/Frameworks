import React, { Component } from "react";
import InputRange from "react-input-range";
import "react-input-range/lib/css/index.css";
import { months, years } from "./Constants";
import "./Frameworks.css";
import WordCloud from "react-d3-cloud";

class Wordcloud extends Component {
  constructor(props) {
    super(props);

    const { framework } = props;

    this.state = {
      framework,
      data: require(`./data/${framework}_words.json`),
      value: { min: 0, max: 47 },
      words: []
    }
    this.calculateWordCloud(this.state.value, true);
  }

  formatLabel = value => {
    if (value < 0) value = 0;
    if (value > 47) value = 47;
    const month = months[value % 12];
    const year = years[Math.floor(value / 12)];
    return `${month} ${year}`;
  }

  calculateWordCloud = (value, firstTime) => {
    const { data } = this.state;
    const minYear = Math.floor(value.min / 12) + 2015;
    const minMonth = value.min % 12 - 1;
    const maxYear = Math.floor(value.max / 12) + 2015;
    const maxMonth = value.max % 12;

    let tempYear = minYear,
      tempMonth = minMonth;

    const newWords = {};
    do {
      tempMonth += 1;
      tempYear += Math.floor(tempMonth / 12);
      tempMonth %= 12;

      const tempWords = data[`${tempYear}-${tempMonth}`] || [];
      tempWords.forEach(word => {
        if (newWords[word.text]) newWords[word.text]['value'] += word.value;
        else newWords[word.text] = { value: word.value };
      })
    } while (tempMonth !== maxMonth || tempYear !== maxYear)
    const words = [];
    Object.keys(newWords).forEach(word => {
      words.push({
        text: word,
        value: newWords[word]['value']
      });
    });

    if (!this.mounted) this.state.words = words;
    else this.setState({ words });
  }

  componentWillMount = () => this.mounted = true;

  render() {
    const { words } = this.state;

    return (
      <div>
        <WordCloudWrapper
          data={this.state.words}
          fontSizeMapper={word => Math.log2(word.value) * 10}
          rotate={word => word.value % 360}
        />
        <div className="slider">
          <InputRange
            allowSameValues
            draggableTrack
            minValue={0}
            maxValue={47}
            value={this.state.value}
            onChange={value => {
              if (value.min < 0) value.min = 0;
              if (value.max < 0) value.max = 0;
              if (value.min > 47) value.min = 47;
              if (value.max > 47) value.max = 47;
              this.setState({ value })
            }}
            onChangeComplete={this.calculateWordCloud}
            formatLabel={this.formatLabel}
          />
        </div>
      </div>)
  }
}

class WordCloudWrapper extends Component {
  shouldComponentUpdate(nextProps, nextState) {
    if (nextProps.data !== this.props.data) return true;
    return false;
  }
  render() {
    return <WordCloud {...this.props} />
  }
}

export default Wordcloud;