import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./styles.css";
import Header from "../../Components/header";

const Home = () => {
  const [loggedInUser, setLoggedInUser] = useState("");

  useEffect(() => {
    const username = localStorage.getItem("username");
    if (username) {
      setLoggedInUser(username);
    }
  }, []);

  return (
    <>
      <div className="header-home">
        <Header />
      </div>
      <div className="home-container">
        <header className="header">
          <h1>Veja as informações</h1>
        </header>

        <section className="cards-section">
          <Link to="/temperatura" className="card">
            <h4>Temperatura</h4>
            <p>Ver Dados</p>
          </Link>
          <Link to="/umidade" className="card">
            <h4>Umidade</h4>
            <p>Ver Dados</p>
          </Link>
          <Link to="/contador" className="card">
            <h4>Contador</h4>
            <p>Ver Dados</p>
          </Link>
          <Link to="/luminosidade" className="card">
            <h4>Luminosidade</h4>
            <p>Ver Dados</p>
          </Link>
        </section>
      </div>
    </>
  );
};

export default Home;
