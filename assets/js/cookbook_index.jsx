import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { connect, Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk';
import promise from 'redux-promise';
import { createStore, applyMiddleware, combineReducers } from 'redux';

import axios from 'axios'

import { RecipesList } from './cookbook/components/recipes_list'
import { AlertsMenu, AlertsMenuButton } from './cookbook/components/menu';
import { AlertsReducer } from './cookbook/reducers/alerts';

const reducers = combineReducers({
	alerts: AlertsReducer
});

const store = createStore(
	reducers, applyMiddleware(thunkMiddleware, promise)
);



export class App extends Component {
	constructor(props){
		super(props);

		this.state = { recipes: [] }
		axios.get('http://127.0.0.1:8000/cookbook/api/v1/recipe/', {

		}).then(response => {
			this.setState({recipes: response.data})
		});
	}

	render(){
		return (
			<div>
				<RecipesList recipes={this.state.recipes} />
			</div>
		);
	}
}

ReactDOM.render(<Provider store={ store }>
	<AlertsMenu />
</Provider>, document.getElementById('page'))

ReactDOM.render(<Provider store={ store }>
	<AlertsMenuButton />
</Provider>,document.getElementById('menu-button'))

ReactDOM.render(<App />, document.getElementById('cuerpo'))
