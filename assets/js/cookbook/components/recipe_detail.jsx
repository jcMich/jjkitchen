import  React from 'react';
import { Link } from 'react-router';

export class RecipeDetail extends React.Component {

    render(){
        const recipes = this.props.recipes || [];
        const recipe_pk  = this.props.params.recipe;
        let receta = {}

        recipes.map(recipe => {
            if (recipe.pk === parseInt(recipe_pk)){
                receta = recipe;
            }
        });

        let ingredients = null;
        if (receta.pk){
            const ingredients_list = receta.ingredients;
            ingredients = ingredients_list.map(ingredient => {
                return <li key={Math.random()}><bold>{ingredient.ingredient.name}</bold> { ingredient.used } {ingredient.unit}</li>
            })
        }
        debugger;
        const recipe_ren = receta.pk ? <div className="jumbotron">
            <img src={receta.image || 'http://127.0.0.1:8000/media/defaults/jj.svg'} className="img-fluid w-100" alt={receta.title}/>
            <h1 className="display-3"> { receta.title }</h1>
            <p className="lead"> { receta.description }</p>
            <hr className="my-2" />
            <h4> Ingredients</h4>
                <ul>
                    { ingredients }
                </ul>
            <h4> Directions</h4>
            <p> { receta.directions }</p>
            <p className="lead">
                <Link to='/' className='btn btn-primary'>Recipes list</Link>
            </p>
        </div> : <div></div>
        return (
                <div>
                    { recipe_ren }
                </div>
        );
    };
}
