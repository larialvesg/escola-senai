import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import './styles.css';

export default function Header() {
  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/';
  };

  const [loggedInUser, setLoggedInUser] = useState("");

  useEffect(() => {
    const username = localStorage.getItem("username");
    if (username) {
      setLoggedInUser(username);
    }
  }, []);

  return (
    <div className="container_header">
      <section className="body">
        <div className="title">
          <h2>Ordem de serviço</h2>
        </div>
        <div className="user-info">
          <p>Bem-vindo, {loggedInUser || "Convidado"}!</p>
          <button className="login-botao" onClick={logout}>Logout</button>
        </div>
      </section>
    </div>
  );
}
