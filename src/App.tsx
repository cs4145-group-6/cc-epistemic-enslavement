import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';
import './App.css';
import MainPage from "./pages/MainPage.tsx";

const App = () => {
  return (
    // Route to specific pages based on URL path
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
