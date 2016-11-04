var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
	context: __dirname,

	entry: './assets/js/cookbook_index',
	output: {
		path: path.resolve('./assets/bundles/'),
		filename: '[name]-[hash].js'
	},
	plugins: [
		new BundleTracker({
			filename: './webpack-stats.json'
		})
	],
	resolve: {
		moduleDirectories: ['node_modules'],
		extensions: ['', '.js', '.jsx']
	},
	module: {
		loaders: [
			{
				test: /\.jsx?$/,
				exclude: /node_modules/,
				loader: 'babel-loader',
				query: {
					presets: ['es2015', 'react']
				}
			},
		]
	}
}
