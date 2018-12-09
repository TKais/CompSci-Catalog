var UglifyJsPlugin = require("uglifyjs-webpack-plugin");
var MiniCssExtractPlugin = require("mini-css-extract-plugin");
var OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

module.exports = {
  entry: [
    './assets/css/main.scss'
  ],
  output: {
    path: __dirname + '/public',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          process.env.NODE_ENV !== 'production' ? 'style-loader' : MiniCssExtractPlugin.loader,
          "css-loader",
          "sass-loader"
        ]
      }
    ]
  },
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true,
        sourceMap: true // set to true if you want JS source maps
      }),
      new OptimizeCSSAssetsPlugin({})
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
      chunkFilename: "[id].css"
    })
  ],
};