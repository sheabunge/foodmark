var initMap=function(){var a={lat:-42.881973,lng:147.3281693},b=new google.maps.Map(document.getElementById("map"),{zoom:16,center:a}),c=[];produce.forEach(function(a){var d={lat:a.lat,lng:a.long},e=addMarker(d,b,a);console.log(e),c.push(e)})},addMarker=function(a,b,c){var d={url:"/static/images/mark.png",origin:new google.maps.Point(0,0),anchor:new google.maps.Point(42,66)},e=new google.maps.Marker({position:a,icon:d,title:c.type+" "+c.species+"\n"+c.desc+" - $"+c.price,map:b});return google.maps.event.addListener(e,"click",function(a){window.location.href="/produce/"+c.id}),e};
//# sourceMappingURL=maps.js.map