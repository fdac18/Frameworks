import React from "react";
import "./Frameworks.css";

const Footer = () => {
  const width = Math.max(document.body.clientWidth, window.innerWidth || 0);
  return (
    <div className="footer">
      <a href="https://steamcommunity.com/id/MikeynJerry">About Us</a>
      <a href="https://github.com/fdac18/Frameworks">{width < 450 ? "Learn more" : "Learn more about our project"}</a>
      <a href="mailto:jdunca51@vols.utk.edu?subject=Frameworks">Email Us</a>
    </div>
  );
};

export default Footer;