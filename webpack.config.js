const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const path = require('path')
/** @type {import('webpack').Configuration;} */
module.exports = {
    entry: "./page/index.js",
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: 'app.bundle.js',
        publicPath: ""
    }, 
    mode: "development",
    module: {
        rules: [
            {
            use: "babel-loader",
            test: /.(js|jsx)$/,
            exclude: /node_modules/,
            }
        ]
    }, 
    resolve: {
        extensions: [".js", ".jsx", ".json"],
    },
    devServer: {
        port: 4000,
        watchFiles: path.resolve(__dirname, 'static/dist'),
        
    },
    plugins: [
        new CleanWebpackPlugin()
    ]
};