import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./Frameworks.css";
import Card from "@material-ui/core/Card";
import CardMedia from "@material-ui/core/CardMedia";
import CardActionArea from "@material-ui/core/CardActionArea";
import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";
import AngularImg from "./assets/Angular.jpg";
import ReactImg from "./assets/React.png";
import VueImg from "./assets/Vue.png";
import jQueryImg from "./assets/jQuery.jpg";
import EmberImg from "./assets/Ember.jpeg";
import BackboneImg from "./assets/Backbone.png";

class Homepage extends Component {
  render() {
    const styles = {
      cardImage: {
        height: "calc((100vh - 90px - 50px)/2)"
      }
    };

    const frameworks = [
      { image: AngularImg, title: "Angular", link: "angular" },
      { image: ReactImg, title: "React", link: "react" },
      { image: VueImg, title: "Vue", link: "vue" },
      { image: jQueryImg, title: "jQuery", link: "jquery" },
      { image: EmberImg, title: "Ember.js", link: "ember" },
      { image: BackboneImg, title: "Backbone", link: "backbone" }
    ].sort(() => Math.random() - 0.5);

    return (
      <div style={styles.container}>
        <GridList
          cellHeight={"auto"}
          cols={3}
          spacing={0}
          style={{ alignItems: "stretch" }}
        >
          {frameworks.map((framework, i) => (
            <GridListTile key={i}>
              <Card>
                <Link to={framework.link} style={{ color: "#ffffff" }}>
                  <CardActionArea>
                    <CardMedia
                      style={styles.cardImage}
                      image={framework.image}
                      title={framework.title}
                    />
                  </CardActionArea>
                </Link>
              </Card>
            </GridListTile>
          ))}
        </GridList>
      </div>
    );
  }
}

export default Homepage;
