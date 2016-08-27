

var initMap = function () {

    var location = { lat: -42.881973, lng: 147.3281693 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: location
    });

    google.maps.event.addListener(map, 'click', function(event) {
        addMarker(event.latLng, map);
    });

    addMarker(location, map);
};

var addMarker = function (location, map) {
    var markerSize = 64;

    var markerIcon = {
        url: '/static/images/mark.svg',
        size: new google.maps.Size(markerSize, markerSize),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(markerSize/2, markerSize/2)
    };

    // Add the marker at the clicked location, and add the next-available label
    // from the array of alphabetical characters.
    var marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: markerIcon
    });

    google.maps.event.addListener(marker, 'click', function (event) {
        window.location.href = '/marker/';
    });
};
