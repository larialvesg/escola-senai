import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./styles.css";

export default function Header() {
  const navigate = useNavigate();

  const [loggedInUser, setLoggedInUser] = useState("");

  useEffect(() => {
    const username = localStorage.getItem("username");
    if (username) {
      setLoggedInUser(username);
    }
  }, []);

  function handleClick() {
    navigate("/home");
  }

  const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    window.location.href = "/";
  };

  return (
    <div className="container_header">
      <section className="body">
        <div className="title">
          <h2 onClick={handleClick}>Ordem de serviço</h2>
        </div>
        <div className="user-info">
          <p>Bem-vindo, {loggedInUser || "Convidado"}!</p>
          <button className="login-botao" onClick={logout}>
            Logout
          </button>
        </div>
      </section>
    </div>
  );
}
