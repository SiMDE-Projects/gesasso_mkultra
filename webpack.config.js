const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MomentLocalesPlugin = require('moment-locales-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TsconfigPathsPlugin = require('tsconfig-paths-webpack-plugin');

module.exports = {
  entry: {
    frontend: './gesasso/frontend/src/index.tsx',
  },
  devtool: 'inline-source-map',
  output: {
    path: path.resolve('./gesasso/frontend/dist'),
    filename: '[name]-[chunkhash].js',
    publicPath: '/static/',
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MomentLocalesPlugin({
      localesToKeep: ['fr'],
    }),
    new BundleTracker({
      path: __dirname,
      filename: './gesasso/frontend/webpack-stats.json',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|venv)/,
        use: {
          loader: 'babel-loader',
          options: { presets: ['@babel/env', '@babel/preset-react'] },
        },
      },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /(node_modules|venv)/,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          {
            loader: 'url-loader',
          },
        ],
      },
    ],
  },
  devServer: {
    devMiddleware: {
      writeToDisk: true,
    },
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.ts', '.tsx'],
    plugins: [new TsconfigPathsPlugin()],
    alias: {
      '@gesasso': path.resolve(__dirname, 'gesasso/frontend/src'),
    },
  },
};
