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

    let multiplier;
    const width = Math.max(document.body.clientWidth, window.innerWidth || 0);
    if (width > 1000) {
      multiplier = 10;
    } else if (width > 500) {
      multiplier = 5;
    } else {
      multiplier = 3;
    }

    this.state = {
      framework,
      data: require(`./data/${framework}_words.json`),
      value: { min: 22, max: 25 },
      words: [],
      multiplier
    }
  }

  componentDidMount() {
    this.calculateWordCloud(this.state.value);
  }

  formatLabel = value => {
    if (value < 0) value = 0;
    if (value > 46) value = 46;
    const month = months[value % 12];
    const year = years[Math.floor(value / 12)];
    return `${month} ${year}`;
  }

  calculateWordCloud = value => {
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

      const tempWords = data[`${tempYear}-${(tempMonth + 1).toString().padStart(2, '0')}`] || [];
      tempWords.forEach(word => {
        if (newWords[word.text]) newWords[word.text]['value'] += word.value;
        else newWords[word.text] = { value: word.value };
      })
    } while (tempMonth !== maxMonth || tempYear !== maxYear);

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
          data={words}
          fontSizeMapper={word => Math.log2(word.value) * this.state.multiplier}
          rotate={word => word.value % 160 - 80}
          width={this.props.width}
          height={this.props.height - 40}
        />
        <div className="slider">
          <InputRange
            allowSameValues
            draggableTrack
            minValue={0}
            maxValue={46}
            value={this.state.value}
            onChange={value => {
              if (value.min < 0) value.min = 0;
              if (value.max < 0) value.max = 0;
              if (value.min > 46) value.min = 46;
              if (value.max > 46) value.max = 46;
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
    if (nextProps.height !== this.props.height) return true;
    if (nextProps.width !== this.props.width) return true;
    return false;
  }
  render() {
    return <WordCloud {...this.props} />
  }
}

export default Wordcloud;