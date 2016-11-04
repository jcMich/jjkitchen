export const TOGGLE_ALERTS = 'TOGGLE_ALERTS';

export const toggleAlerts = (isOpen) => {
	return (dispatch) => {
		return dispatch({
			type: TOGGLE_ALERTS,
			payload: isOpen
		});
	};
};