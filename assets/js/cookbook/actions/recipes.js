export const FETCH_RECIPES = 'FETCH_RECIPES';
import axios from 'axios'

export const fetchRecipes = () => {
	return dispatch => {
		return axios.get('http://127.0.0.1:8000/cookbook/api/v1/recipe/', {
		}).then( response => {
			return dispatch({
				type: FETCH_RECIPES,
	 			payload: response.data
			});
		});
	};
};
