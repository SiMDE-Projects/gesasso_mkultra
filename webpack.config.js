const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports = {
  entry: {
    frontend: './gesasso/frontend/src/index.js',
  },
  output: {
    path: path.resolve('./gesasso/frontend/dist'),
    filename: '[name]-[hash].js',
    publicPath: '/static/',
  },
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({
      path: __dirname,
      filename: './gesasso/frontend/webpack-stats.json',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
            loader: "babel-loader",
            options: {presets: ["@babel/env", "@babel/preset-react"]}
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devServer: {
    devMiddleware: {
        writeToDisk: true,
    },
  },
}
