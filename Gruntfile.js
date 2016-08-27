module.exports = function(grunt) {
	'use strict';

	require('load-grunt-tasks')(grunt);

	grunt.initConfig({

		watch: {

			css: {
				files: ['static/css/**/*.css'],
				tasks: ['postcss']
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

		clean: {
			options: {
				force: true
			},
			dist: ['static/dist/']
		}
	});

	grunt.registerTask('default', ['clean', 'postcss']);
};
