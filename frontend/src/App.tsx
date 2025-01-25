import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Upload from "./components/Upload";
import Review from "./components/Review";
import './style.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Upload />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/review" element={<Review />} />
      </Routes>
    </Router>
  );
}

export default App;