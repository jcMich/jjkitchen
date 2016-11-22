import { TOGGLE_ALERTS } from '../actions/menu';

export const AlertsReducer = (state=false, action) => {
	switch(action.type)
	{
	case TOGGLE_ALERTS:
		return action.payload;
	default:
		return state;
	}
}
