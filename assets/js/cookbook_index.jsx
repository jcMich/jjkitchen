import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { connect, Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk';
import promise from 'redux-promise';
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { Router, Route, hashHistory, IndexRoute } from 'react-router';
import { reducer as formReducer } from 'redux-form'

import { RecipesList } from './cookbook/components/recipes_list'
import { AlertsMenu, AlertsMenuButton } from './cookbook/components/menu';
import { RecipeDetail } from './cookbook/components/recipe_detail';
import { AlertsReducer } from './cookbook/reducers/menu';
import { RecipesReducer } from './cookbook/reducers/recipes';
import { fetchRecipes } from './cookbook/actions/recipes';

import { RecipeForm } from './cookbook/components/add_recipe';

const reducers = combineReducers({
	recipes: RecipesReducer,
	alerts: AlertsReducer,
	form: formReducer,
});

const store = createStore(
	reducers, applyMiddleware(thunkMiddleware, promise)
);

class App extends Component {
	componentWillMount(){
		const { dispatch } = this.props;
		dispatch(fetchRecipes());
	}
	handleReciptSubmit(values){
		console.log(values);
	}

	render(){
		const { children } = this.props;

		return (
			<div>
				<div id="page">
					<AlertsMenu />
				</div>
		        <div className='row'>
		            <div id="menu-button" style={{position: "absolute", left: "15px", top: "20px"}} >
						<AlertsMenuButton />
		            </div>
		        </div>
		        <div id="cuerpo" className='container bs-docs-container'>
		        	{ React.cloneElement(children, { ...this.props, onSubmit: this.handleReciptSubmit })}
		        </div>
			</div>
		);
	}
}

export const AppConected = connect( store => {
	return {
		recipes: store.recipes
	}
})(App);

ReactDOM.render(<Provider store={ store }>
	<Router history={hashHistory}>
		<Route path='/' component={ AppConected } >
			<IndexRoute component={ RecipesList  } />
			<Route path='/add' component={ RecipeForm } />
			<Route path='/detail/:recipe' component={ RecipeDetail } />
		</Route>
	</Router>
</Provider>, document.getElementById('container'))

