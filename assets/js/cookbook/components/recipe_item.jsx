import  React from 'react';
import { Link } from 'react-router';

export const RecipeItem = ({recipe}) => {
	return (
		 <div className="card" style={{ marginTop: '20px'}}>
		    <img className="card-img-top img-fluid" src={ recipe.image || 'http://127.0.0.1:8000/media/defaults/jj.svg' } alt="Card image cap" />
		    <div className="card-block">
		      <h4 className="card-title">{ recipe.title }</h4>
		      <p className="card-text">{ recipe.description }</p>
		      <Link to={`/detail/${recipe.pk}`}>
		      	<small className="text-muted" style={{ color: 'grey'}}>View more</small>
		      </Link>
		    </div>
		  </div>
	);
}
