import { FETCH_RECIPES } from '../actions/recipes';

export const RecipesReducer = (state=false, action) => {
	switch(action.type)
	{
	case FETCH_RECIPES:
		return action.payload;
	default:
		return state;
	}
}
