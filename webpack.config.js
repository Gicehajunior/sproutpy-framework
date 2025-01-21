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
                    { from: './node_modules/bootstrap/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/bootstrap/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/bootstrap-datepicker/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/bootstrap-datepicker/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/print-js/dist/*.css', to: 'asst/printjs/css/[name][ext]' },
                    { from: './node_modules/print-js/dist/*.js', to: 'asst/printjs/js/[name][ext]' },
                    { from: './node_modules/select2/dist/css/*.css', to: 'bootstrap/css/[name][ext]' },
                    { from: './node_modules/select2/dist/js/*.js', to: 'bootstrap/js/[name][ext]' },
                    { from: './node_modules/toastr/build/*.css', to: 'asst/toastr/css/[name][ext]' },
                    { from: './node_modules/toastr/build/*.js', to: 'asst/toastr/js/[name][ext]' }, 
                    { from: './node_modules/chart.js/dist/*.js', to: 'asst/charts/js/[name][ext]' },
                    { from: './node_modules/sweetalert2/dist/*.css', to: 'asst/sweetalert/css/[name][ext]' },
                    { from: './node_modules/sweetalert2/dist/*.js', to: 'asst/sweetalert/js/[name][ext]' },
                    { from: './node_modules/popper.js/dist/*.js', to: 'asst/js/[name][ext]' },
                    { from: './node_modules/datatables/media/css/*.css', to: 'asst/jquery/css/[name][ext]' },
                    { from: './node_modules/datatables/media/js/*.js', to: 'asst/jquery/js/[name][ext]' },
                    { from: './node_modules/jquery/dist/*.js', to: 'asst/jquery/js/[name][ext]' },
                    { from: './node_modules/datatables/media/images', to: 'asst/jquery/images' },
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
