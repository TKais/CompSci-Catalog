var webpack = require('webpack');
var path = require('path');

module.exports = {  
  entry: [
    './js/app.js'
  ],
  output: {
    path: __dirname + '/js',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /.jsx?$/,
        loaders: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        },
      }
    ]
  },
  plugins: [
  ]
};