require('dotenv').config();
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = (env, argv) => {
    const mode = argv.mode || process.env.APP_ENV || 'production';
    
    return {
        mode: mode,
        entry: {},
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
                    { from: './node_modules/bootstrap/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/bootstrap/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/bootstrap-datepicker/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/bootstrap-datepicker/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/print-js/dist/*.css', to: 'static/printjs/css/[name][ext]' },
                    { from: './node_modules/print-js/dist/*.js', to: 'static/printjs/js/[name][ext]' },
                    { from: './node_modules/select2/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/select2/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/toastr/build/*.css', to: 'static/toastr/css/[name][ext]' },
                    { from: './node_modules/toastr/build/*.js', to: 'static/toastr/js/[name][ext]' }, 
                    { from: './node_modules/chart.js/dist/*.js', to: 'static/charts/js/[name][ext]' },
                    { from: './node_modules/sweetalert2/dist/*.css', to: 'static/sweetalert/css/[name][ext]' },
                    { from: './node_modules/sweetalert2/dist/*.js', to: 'static/sweetalert/js/[name][ext]' },
                    { from: './node_modules/popper.js/dist/*.js', to: 'static/js/[name][ext]' },
                    { from: './node_modules/datatables/media/css/*.css', to: 'static/jquery/css/[name][ext]' },
                    { from: './node_modules/datatables/media/js/*.js', to: 'static/jquery/js/[name][ext]' },
                    { from: './node_modules/jquery/dist/*.js', to: 'static/jquery/js/[name][ext]' },
                    { from: './node_modules/datatables/media/images', to: 'static/jquery/images' },
                    // ADD NEW RESOURCE TO BE COPIED HERE IF NEEDED.
                ]
            })
        ],
        resolve: {
            extensions: ['.js', 'css']
        },
        devtool: 'source-map' // Optional, for easier debugging
    };
};
