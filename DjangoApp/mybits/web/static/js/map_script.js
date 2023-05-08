// Get the map element and set the center and zoom level
maptilersdk.config.apiKey = 'EIHtGfd43qFxkWQe23Uj';

var map = new maptilersdk.Map({
    container: 'map',
    style: maptilersdk.MapStyle.HYBRID,
    geolocate: maptilersdk.GeolocationType.POINT
});

map.on('load', function () {
    map.loadImage(
        'https://docs.maptiler.com/sdk-js/assets/custom_marker.png',
        // Add an image to use as a custom marker
        function (error, image) {
            if (error) throw error;
            map.addImage('custom-marker', image);

            map.addSource('places', {
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': [
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>Restaurant Masia Les Garrigues</strong><p>Make it Mount Pleasant is a handmade and vintage market and afternoon of live entertainment and kids activities. 12:00-6:00 p.m.</p>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [0.878970, 41.511622]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>Escola Politècnica Superior</strong><p>Head to Lounge 201 (201 Massachusetts Avenue NE) Sunday for a Mad Men Season Five Finale Watch Party, complete with 60s costume contest, Mad Men trivia, and retro food and drink. 8:00-11:00 p.m. $10 general admission, $20 admission and two hour open bar.</p>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [0.623511, 41.608998]
                            }
                        },
                        {
                            'type': 'Feature',
                            'properties': {
                                'description':
                                    '<strong>Truckeroo</strong><p>Truckeroo brings dozens of food trucks, live music, and games to half and M Street SE (across from Navy Yard Metro Station) today from 11:00 a.m. to 11:00 p.m.</p>'
                            },
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-77.007481, 38.876516]
                            }
                        }
                    ]
                }
            });

            // Add a layer showing the places.
            map.addLayer({
                'id': 'places',
                'type': 'symbol',
                'source': 'places',
                'layout': {
                    'icon-image': 'custom-marker',
                    'icon-overlap': 'always'
                }
            });
        }
    );

    // Create a popup, but don't add it to the map yet.
    var popup = new maptilersdk.Popup({
        closeButton: false,
        closeOnClick: false
    });

    map.on('mouseenter', 'places', function (e) {
        // Change the cursor style as a UI indicator.
        map.getCanvas().style.cursor = 'pointer';

        var coordinates = e.features[0].geometry.coordinates.slice();
        var description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        // Populate the popup and set its coordinates
        // based on the feature found.
        popup.setLngLat(coordinates).setHTML(description).addTo(map);
    });

    map.on('mouseleave', 'places', function () {
        map.getCanvas().style.cursor = '';
        popup.remove();
    });
});