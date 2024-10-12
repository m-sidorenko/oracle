import React from 'react';
import styles from './HomePage.module.css';
import { Link } from 'react-router-dom';

const HomePage = () => {
	return (
		<div className={styles.container}>
			<div className={styles.header}>
				<h1 className={styles.headerTitle}>Таро дня</h1>
			</div>
			<img src="https://raw.githubusercontent.com/izyryanova/oracle-tarot/refs/heads/main/public/icon/sun.png" className={styles.mainImg} alt="Sun" />
			<Link to="/select-card" className={styles.btnClick}>
				Выбери свою <br /> карту дня
			</Link>
		</div>
	);
};

export default HomePage;