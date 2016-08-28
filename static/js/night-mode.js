
(function () {
    'use strict';

    var toggleButton = document.querySelector('.toggle-night');
    var classes = document.body.classList;
    var ground = document.getElementById('ground');

    var setDay = function () {
        toggleButton.innerHTML = '<span class="fa fa-moon-o"></span>';
        classes.remove('night');
        classes.add('day');
        ground.src = '/static/images/ground.svg';
    };

    var setNight = function () {
        toggleButton.innerHTML = '<span class="fa fa-sun-o"></span>';
        classes.remove('day');
        classes.add('night');
        ground.src = '/static/images/ground-night.svg';
    };

    toggleButton.onclick = function () {
        if (document.body.classList.contains('night')) {
            setDay();
        } else {
            setNight();
        }
    };

    setDay();
})();
