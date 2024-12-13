import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';
import './App.css';
// @ts-ignore
import MainPage from "./pages/MainPage.tsx";

const App = () => {
  return (
    // Route to specific pages based on URL path
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
		<Route path="*" element={<MainPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
