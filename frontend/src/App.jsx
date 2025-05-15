import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Pages/Login/in/index";
import Signup from "./Pages/Login/up/index";
import Home from "./Pages/Home";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login/up" element={<Signup />} />
        <Route path="/home" element={<Home/>} />
      </Routes>
    </Router>
  );
};

export default App;