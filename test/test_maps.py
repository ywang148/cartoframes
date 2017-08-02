"""Unit tests for cartoframes.layers"""
import unittest
from cartoframes.layer import BaseMap, Layer, QueryLayer
from cartoframes.maps import non_basemap_layers, has_time_layer, get_map_name, get_map_template
from cartoframes.layer import BaseMap


class TestMaps(unittest.TestCase):
    """ Tests for functions in maps module"""
    def setUp(self):
        self.layers = [BaseMap('dark'),
                       Layer('cb_2013_puma10_500k',
                             color='grey'),
                       Layer('tweets_obama',
                             color='yellow',
                             size='favoritescount')
                       ]
        self.nbm_layers = non_basemap_layers(self.layers)
        self.layer_with_time = has_time_layer(self.layers)
        self.map_name = get_map_name(self.layers, has_zoom=False)
        self.map_template = get_map_template(self.layers, has_zoom=False)
        self.js = '{"placeholders": {"north": {"default": 45, "type": "number"}, "cartocss_1": {"default": "#layer { marker-fill: red; marker-width: 5; marker-allow-overlap: true; marker-line-color: #000; }", "type": "sql_ident"}, "cartocss_0": {"default": "#layer { marker-fill: red; marker-width: 5; marker-allow-overlap: true; marker-line-color: #000; }", "type": "sql_ident"}, "west": {"default": -45, "type": "number"}, "east": {"default": 45, "type": "number"}, "sql_0": {"default": "SELECT ST_PointFromText(\'POINT(0 0)\', 4326) as the_geom, 1 as cartodb_id, ST_PointFromText(\'Point(0 0)\', 3857) as the_geom_webmercator", "type": "sql_ident"}, "sql_1": {"default": "SELECT ST_PointFromText(\'POINT(0 0)\', 4326) as the_geom, 1 as cartodb_id, ST_PointFromText(\'Point(0 0)\', 3857) as the_geom_webmercator", "type": "sql_ident"}, "south": {"default": -45, "type": "number"}}, "version": "0.0.1", "name": "cartoframes_ver20170406_layers2_time0_baseid1_labels0_zoom0", "layergroup": {"layers": [{"type": "http", "options": {"urlTemplate": "https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png", "subdomains": "abcd"}}, {"type": "mapnik", "options": {"cartocss": "<%= cartocss_0 %>", "sql": "<%= sql_0 %>", "cartocss_version": "2.1.1"}}, {"type": "mapnik", "options": {"cartocss": "<%= cartocss_1 %>", "sql": "<%= sql_1 %>", "cartocss_version": "2.1.1"}}], "version": "1.0.1"}, "view": {"bounds": {"west": "<%= west %>", "east": "<%= east %>", "north": "<%= north %>", "south": "<%= south %>"}}}'

    def test_non_basemap_layers(self):
        self.assertEqual(self.layers[1],
                         self.nbm_layers[0])

        self.assertEqual(self.layers[2],
                         self.nbm_layers[1])

    def test_has_time_layer(self):
        self.assertEqual(self.layer_with_time, False)

    def test_get_map_name(self):
        self.assertEqual(self.map_name,
                         'cartoframes_ver20170406_layers2_time0_baseid1_labels0_zoom0')

    def test_map_template(self):
        self.assertEqual(self.map_template,
                         self.js)
