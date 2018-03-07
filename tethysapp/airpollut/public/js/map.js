var map, view, dem, roadsLayer, demLayerBox, roadsLayerBox;


function toggleDEM() {
    dem.visible = demLayerBox.checked;
}

// Get esri arcmap
require([
        "esri/Map",
        "esri/views/MapView",
        "esri/layers/FeatureLayer",
        "esri/layers/MapImageLayer",
        "dojo/on",
        "dojo/dom",
        "dojo/_base/lang",
        "dojo/domReady!"
    ],
    (Map, MapView, FeatureLayer, MapImageLayer, on, dom, lang) => {

        roadsLayerBox = document.querySelector('input[id="roadsLayer"]');
        demLayerBox = document.querySelector('input[id="demLayer"]');

        var template = {
            title: "Street Info for: {fullname}",
            content: "<p>Street Name: {fullname}</p> <p>Zip: {zipcode_l}</p> <p>Speed Limit: {speed_lmt}</p>"
        };

        dem = new MapImageLayer({
            url: "http://geoserver2.byu.edu/arcgis/rest/services/Valor/Elevations/MapServer"
        });
        dem.opacity = 0.5;
        roadsLayer = new FeatureLayer({
            url: "http://geoserver2.byu.edu/arcgis/rest/services/Valor/MyMapService/FeatureServer/0",
            outFields: ["*"],
            popupTemplate: template

        });

        map = new Map({
            basemap: "streets",
            layers: [dem, roadsLayer]
        });
        view = new MapView({
            container: "map",
            center: [-111.659274, 40.232873],
            zoom: 15,
            map: map
        });

        $('input[id=demLayer]').on('switchChange.bootstrapSwitch', function (event, state) { dem.visible = demLayerBox.checked; });
        $('input[id=roadsLayer]').on('switchChange.bootstrapSwitch', function (event, state) { roadsLayer.visible = roadsLayerBox.checked; });

        // on(dom.byId("demLayer"), "change", function() { dem.visible = demLayerBox.checked; });
        // on(dom.byId("roadsLayer"), "change", function() { roadsLayer.visible = roadsLayerBox.checked; });


    });
