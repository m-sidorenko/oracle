import React from 'react';
import styles from './CardDescription.module.css';
import { Link } from 'react-router-dom';

const CardDescription = () => {
	return (
		<div className={styles.container}>
			{/* Описание карты и кнопки */}
			<Link to="/store-menu" className={styles.btnBack}>Назад</Link>
			<Link to="/daily-spread" className={styles.btnSpread}>Расклад дня</Link>
		</div>
	);
};

export default CardDescription;