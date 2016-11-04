import React from 'react';
import { connect } from 'react-redux';
import { push as Menu } from 'react-burger-menu';

import { toggleAlerts } from '../actions/alerts';


const MenuButton = (props) => {
	const handleClick = () => {
		props.dispatch(toggleAlerts(!props.isOpen));
	}

	return (
		<a onClick={ handleClick.bind(this)} href="javascript:;">
			<i className="fa fa-list fa-2x" />
		</a>
	);
};

export const AlertsMenuButton = connect( store => ({
	isOpen: store.alerts
}))(MenuButton);


const AlertsBurgerMenu = (props) => {

	return(
		<Menu
		pageWrapId={ "cuerpo" }
		outerContainerId={ "container" }
		isOpen={props.isOpen}
		customBurgerIcon={ false }
		customCrossIcon={ false }
		onStateChange={ (state) => {
			if( state.isOpen !== props.isOpen){
				props.dispatch(toggleAlerts(state.isOpen))
			}
		}}
		>
			<a href='#'> <i className='fa fa-archive'/><span><strong>Add Recipe</strong></span></a>
			<a href='#'> <i className='fa fa-archive'/><span><strong>Add Ingredient</strong></span></a>
			<a href='#'> <i className='fa fa-eye'/><span><strong>Show Ingredients</strong></span></a>
		</Menu>
	);
};

export const AlertsMenu = connect(store => ({
	isOpen: store.alerts
}))(AlertsBurgerMenu);
