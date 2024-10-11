import React from 'react';
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './Components/HomePage/HomePage';
import CardSelectionGrid from './Components/CardSelectionGrid/CardSelectionGrid';
import CardDescription from './Components/CardDescription/CardDescription';
import StoreMenu from './Components/StoreMenu/StoreMenu';
import DailyLayout from './Components/DailyLayout/DailyLayout';

const App = () => {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/select-card" element={<CardSelectionGrid />} />
				<Route path="/card-detail" element={<CardDescription />} />
				<Route path="/store-menu" element={<StoreMenu />} />
				<Route path="/daily-spread" element={<DailyLayout />} />
			</Routes>
		</Router>
	);
};

export default App;