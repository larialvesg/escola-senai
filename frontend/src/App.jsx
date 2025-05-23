import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Pages/Login/in/index";
import Signup from "./Pages/Login/up/index";
import Home from "./Pages/Home";
import Ambientes from "./Pages/Ambientes";
import Patrimonios from "./Pages/Patrimonios";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login/up" element={<Signup />} />
        <Route path="/home" element={<Home/>} />
        <Route path="/ordemdeservico" element={<Home/>} />
        <Route path="/patrimonios" element={<Patrimonios/>} />
        <Route path="/ambientes" element={<Ambientes/>} />
        <Route path="/manutentores" element={<Home/>} />
      </Routes>
    </Router>
  );
};

export default App;