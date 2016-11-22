import React from 'react'
import { connect } from 'react-redux';

import { RecipeItem } from '../components/recipe_item';
import { fetchRecipes } from '../actions/recipes';

class Recipes extends React.Component {
    componentWillMount(){
	debugger;
        const { dispatch } = this.props;
        dispatch(fetchRecipes());
    }
    render(){
        const recipes = this.props.recipes || [];
        const recipes_items = recipes.map((recipe)  => {
            return (
                <RecipeItem recipe={ recipe } key={recipe.pk}/>
            );
        });

        return (
            <div className='card-columns'>
                { recipes_items }
            </div>
        );
    }
}

export const RecipesList =  connect(store => ({
    recipes: store.recipes,
}))(Recipes);
