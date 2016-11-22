import React from 'react';
import { Field, FieldArray, formValueSelector, reduxForm } from 'redux-form';
import { connect } from 'react-redux';
import Dropzone  from 'react-dropzone';


const renderField = ({ input, label, col, type, meta: { touched, error } }) => (
  <div>
	<div className={col}>
	  <input {...input} type={type} placeholder={label} className='form-control'/>
	  {touched && error && <span>{error}</span>}
	</div>
  </div>
)

const renderIngredients = ({ fields, meta: { touched, error } }) => (
  <div>
	<div>
	  <i className="fa fa-plus fa-2x" onClick={() => fields.push({})} />
	  {touched && error && <span>{error}</span>}
	</div>
	{fields.map((ingredients, index) =>
	  <div key={index} className="form-group row">
		<Field
		  col='col-md-7'
		  name={`${ingredients}.ingredient.name`}
		  type="text"
		  component={renderField}
		  label="Name"/>
		<Field
		  col='col-md-2'
		  name={`${ingredients}.use`}
		  type="text"
		  component={renderField}
		  label="Use"/>
		<Field
		  col='col-md-2'
		  name={`${ingredients}.unit`}
		  type="text"
		  component={renderField}
		  label="Unit"/>
		<i
		  className='col-md-1 fa fa-trash fa-2x'
		  onClick={() => fields.remove(index)} />
	  </div>
	)}
  </div>
)


class Form extends React.Component {
	constructor(props){
		super(props)
		this.state = {
			b64image: null
		}
	}

	onDrop(files) {
		if(files.length > 0) {
			const file = files[0];
			var reader = new FileReader();
			const _this = this;

			reader.readAsDataURL(file);
			reader.onload = function() {
				_this.props.change('image', this.result)
			};
		}
	}

	render() {
		const { handleSubmit } = this.props;
		const dd_style = {
			height: 270,
			borderWidth: 2,
			borderColor: '#666',
			borderStyle: 'dashed',
			borderRadius: 5
		};
		const image_styles = {width:'100%', height: '100%', objectFit: 'cover'}

		const preview = this.props.image ? <img
			src={ this.props.image }
			style={image_styles}
			className="img-fluid" /> : <p>Upload image</p>;

		return (
			<form onSubmit={handleSubmit} style={{marginTop: '20px'}} >
				<div className='row'>
					<div className='col-md-4'>
						<Dropzone  onDrop={this.onDrop.bind(this)}
							multiple={ false }
							accept='image/*'
							style={dd_style}
							disablePreview={ true }>
							{ preview }
						</Dropzone>
					</div>
					<div className="col-md-8">
						<div className="form-group">
							<Field name="name"
								component="input"
								className="form-control"
								type="text"
								placeholder="Name" />
						</div>
						<div className="form-group">
							<Field name="description"
								component="textarea"
								className="form-control"
								type="text"
								style={{height: '160px'}}
								placeholder="Description" />
						</div>
						<div className="form-group">
							<Field name="dificult"
								component="input"
								className="form-control"
								type="text"
								placeholder="Difilult" />
						</div>
					</div>
				</div>
				<h4>Ingredients</h4>
				<div className="form-group row">
					<FieldArray name="ingredients"
						className="form-control"
						component={renderIngredients}/>
				</div>
				<div className="form-group row">
					<Field name="directions"
						component="textarea"
						className="form-control"
						type="text"
						style={{height: '160px'}}
						placeholder="Directions" />
				</div>
				<button type="submit" className="btn btn-primary">Submit</button>
			</form>
		);
	}
}
export const RecipeReduxForm = reduxForm({
  form: 'recipe' // a unique name for this form
})(Form);

const selector = formValueSelector('recipe') // <-- same as form name
export const RecipeForm = connect(state => {
    const { image, name} = selector(state, 'image', 'name')
    return { image }
})(RecipeReduxForm)
