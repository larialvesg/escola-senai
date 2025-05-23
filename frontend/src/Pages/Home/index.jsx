import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./styleshome.css";
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
        <header className="header-home">
          <h1>Veja as informações</h1>
        </header>

        <section className="cards-section">
          <Link to="/ordemdeservico" className="card">
            <h4>Ordens de Serviço</h4>
          </Link>
          <Link to="/patrimonios" className="card">
            <h4>Patrimônios</h4>
          </Link>
          <Link to="/ambientes" className="card">
            <h4>Ambientes</h4>
          </Link>
          <Link to="/manutentores" className="card">
            <h4>Manutentores</h4>
          </Link>
        </section>
      </div>
    </>
  );
};

export default Home;
