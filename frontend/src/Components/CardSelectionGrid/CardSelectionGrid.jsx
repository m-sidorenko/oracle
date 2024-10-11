import React from 'react';
import styles from './CardSelectionGrid.module.css';

const CardSelectionGrid = () => {
	return (
		<div>
			<h2 className={styles.header}>Выберите одну карту</h2>
			<div className={styles.grid}>
				{Array.from({ length: 9 }).map((_, index) => (
					<div key={index} className={styles.card}>
						{/* Здесь можно добавить изображение или текст для каждой карты */}
					</div>
				))}
			</div>
		</div>
	);
};

export default CardSelectionGrid;