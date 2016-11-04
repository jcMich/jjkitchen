import  React from 'react';

export const RecipeItem = ({recipe}) => {
	return (
		 <div className="card" style={{ marginTop: '20px'}}>
		    <img className="card-img-top img-fluid" src={ recipe.image || 'http://previews.123rf.com/images/ciawitaly/ciawitaly1310/ciawitaly131000003/23075318-chef-cartoon-character-Stock-Vector-chef.jpg' } alt="Card image cap" />
		    <div className="card-block">
		      <h4 className="card-title">{ recipe.title }</h4>
		      <p className="card-text">{ recipe.description }</p>
		      <small className="text-muted" style={{ color: 'grey'}}>View more</small>
		    </div>
		  </div>
	);
}
