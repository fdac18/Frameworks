import React, { Component } from 'react';
import './App.css';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardActionArea from '@material-ui/core/CardActionArea';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import AngularImg from "./assets/Angular.jpg";
import ReactImg from "./assets/React.png";
import VueImg from "./assets/Vue.png";
import jQueryImg from "./assets/jQuery.jpg";
import EmberImg from "./assets/Ember.jpeg";
import BackboneImg from "./assets/Backbone.png";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: null,
      fetching: true
    };
  }

  render() {

    const styles = {
      cardImage: {
        height: 300,
      }
    }

    const frameworks = [
      { image: AngularImg, title: "Angular" },
      { image: ReactImg, title: "React" },
      { image: VueImg, title: "Vue" },
      { image: jQueryImg, title: "jQuery" },
      { image: EmberImg, title: "Ember.js" },
      { image: BackboneImg, title: "Backbone" }
    ].sort(() => Math.random() - 0.5);

    return (
      <div className="App">
        <div className="App-header">
          <h1 className="App-title">Frameworks</h1>
        </div>
        <div style={styles.container}>
          <GridList cellHeight={300} cols={3} spacing={12}>
            {frameworks.map((framework, i) => (
              <GridListTile key={i}>
                <Card>
                  <CardActionArea>
                    <CardMedia
                      style={styles.cardImage}
                      image={framework.image}
                      title={framework.title}
                    />
                  </CardActionArea>
                </Card>
              </GridListTile>
            )
            )}
          </GridList>
        </div>
      </div>
    );
  }
}

export default App;
