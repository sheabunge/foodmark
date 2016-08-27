module.exports = function(grunt) {
	'use strict';

	require('load-grunt-tasks')(grunt);

	grunt.initConfig({

		watch: {

			css: {
				files: ['static/css/**/*.css'],
				tasks: ['css']
			},

			js: {
				files: ['static/js/**/*.js'],
				tasks: ['js']
			}
		},

		postcss: {
			options: {
				map: true,
				processors: [
					require('precss')(),
					require('autoprefixer')(),
					require('cssnano')()
				]
			},
			dist: {
				expand: true,
				cwd: 'static/css',
				src: ['*.css', '!_*.css'],
				dest: 'static/dist',
				ext: '.css'
			}
		},

		jshint: {
			dist: ['static/js/**/*.js'],
			gruntfile: ['Gruntfile.js']
		},

		uglify: {
			dist: {
				options: {
					sourceMap: true
				},
				files: {
					'static/dist/app.js': [
						'static/js/geo.js'
					],
					'static/dist/maps.js': 'static/js/maps.js'
				}
			}
		},

		clean: {
			options: {
				force: true
			},
			dist: ['static/dist/']
		}
	});

	grunt.registerTask('css', ['postcss']);
	grunt.registerTask('js', ['jshint', 'uglify']);
	grunt.registerTask('default', ['clean', 'css', 'js']);
};
