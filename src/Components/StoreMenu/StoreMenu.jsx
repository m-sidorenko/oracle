import React from 'react';
import styles from './StoreMenu.module.css';
import { Link } from 'react-router-dom';

const StoreMenu = () => {
	return (
		<div className={styles.container}>
			{/* Меню магазина */}
			<Link to="/select-card" className={styles.btnSelect}>Выбери свою карту дня</Link>
		</div>
	);
};

export default StoreMenu;