require('dotenv').config();
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = (env, argv) => {
    const mode = argv.mode || process.env.APP_ENV || 'production';
    
    return {
        mode: mode,
        entry: './public/index.js',
        output: {
            path: path.resolve(__dirname, 'public/')
        },
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env']
                        }
                    }
                }
            ]
        },
        plugins: [
            new CopyWebpackPlugin({
                patterns: [
                    { from: './node_modules/bootstrap/dist/css/bootstrap.min.css', to: 'asst/css' },
                    { from: './node_modules/bootstrap/dist/js/bootstrap.min.js', to: 'asst/js' },
                    { from: './node_modules/popper.js/dist/popper.min.js', to: 'asst/js' },
                    { from: './node_modules/jquery/dist/jquery.js', to: 'asst/jquery' }
                ]
            })
        ],
        resolve: {
            extensions: ['.js']
        },
        devtool: 'source-map' // Optional, for easier debugging
    };
};
