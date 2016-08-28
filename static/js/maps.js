
var initMap = function () {

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: mapLocation
    });

    var markers = [];

    produce.forEach(function (item) {
        var location = { lat: item.lat, lng: item.long };
        var marker = addMarker(location, map, item);
        console.log(marker);
        markers.push(marker);
    } );
};

var addMarker = function (location, map, item) {

	var markerIcon = {
		url: '/static/images/mark.png',
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(28, 46)
	};

	var marker = new google.maps.Marker({
		position: location,
		icon: markerIcon,
        title: item.type + ' ' + item.species + '\n' + item.desc + ' - $' + item.price,
        map: map
	});

	google.maps.event.addListener(marker, 'click', function (event) {
		window.location.href = '/produce/' + item.id;
	});

    return marker;
};
