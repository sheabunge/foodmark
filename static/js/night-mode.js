
(function () {
    'use strict';

    var toggleButton = document.querySelector('.toggle-night');

    var setDay = function () {
        toggleButton.innerHTML = '<span class="fa fa-moon-o"></span>';
        document.body.classList.remove('night').add('day');
    };

    var setNight = function () {
        toggleButton.innerHTML = '<span class="fa fa-sun-o"></span>';
        document.body.classList.remove('day').add('night');
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
