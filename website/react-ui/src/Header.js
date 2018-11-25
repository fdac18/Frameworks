import React from "react";
import { Link } from "react-router-dom";
import "./Frameworks.css";

const Header = () => {
  return (
    <div className="header">
      <h1 className="header-title">
        <Link to="/" style={{ color: "white", textDecoration: "none" }}>
          Frameworks
        </Link>
      </h1>
    </div>
  );
};

export default Header;
