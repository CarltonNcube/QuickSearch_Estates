const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: {
    index: './src/index.js',
    profile: './src/profile.js',
    search: './src/search.js',
    signin: './src/signin.js',
    signup: './src/signup.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js',
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
      chunks: ['index'],
    }),
    new HtmlWebpackPlugin({
      template: './src/profile.html',
      filename: 'profile.html',
      chunks: ['profile'],
    }),
    new HtmlWebpackPlugin({
      template: './src/search.html',
      filename: 'search.html',
      chunks: ['search'],
    }),
    new HtmlWebpackPlugin({
      template: './src/signin.html',
      filename: 'signin.html',
      chunks: ['signin'],
    }),
    new HtmlWebpackPlugin({
      template: './src/signup.html',
      filename: 'signup.html',
      chunks: ['signup'],
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css',
    }),
    new CopyWebpackPlugin({
      patterns: [
        { from: './public', to: './' }, // Copy all files from public directory to dist
      ],
    }),
  ],
};

