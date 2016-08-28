(function () {
	'use strict';

	var lat, long;

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			lat = position.coords.latitude;
			long = position.coords.longitude;
		});
	}

})();
