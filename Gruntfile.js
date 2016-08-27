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

		sass: {
			options: {
				sourceMap: true
			},
			dist: {
				expand: true,
				cwd: 'static/css',
				src: '*.scss',
				dest: 'static/dist',
				ext: '.css'
			}
		},

		postcss: {
			options: {
				map: true,
				processors: [
					require('autoprefixer')(),
					require('cssnano')()
				]
			},
			dist: {
				expand: true,
				cwd: 'static/dist',
				src: '*.css',
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
						'static/js/night-mode.js'
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
		},

		copy: {
			font_awesome: {
				expand: true,
				flatten: true,
				cwd: 'bower_components/font-awesome/fonts',
				src: '**',
				dest: 'static/dist'
			}
		}
	});

	grunt.registerTask('css', ['sass', 'postcss']);
	grunt.registerTask('js', ['jshint', 'uglify']);
	grunt.registerTask('default', ['clean', 'css', 'js', 'copy']);
};
