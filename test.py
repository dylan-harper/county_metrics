import app
import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/api/v1/county"

    def test_all_counties(self):
        """Test to return count of all counties in db"""
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "Number of stored counties": 3193 })

    def test_county_show(self):
        """Test to return county by its zip"""
        response = requests.get(self.URL + "/10001")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "h_index": 96.8, "zip": "10001" })


    def test_counties_mean_statistic(self):
        """Test to return mean index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/mean?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "mean": 99.5 })


    def test_counties_median_statistic(self):
        """Test to return median index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/median?1001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "median": 100.6 })


    def test_counties_stdev_statistic(self):
        """Test to return (sample) standard deviation index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/stdev?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "stdev": 2.35 })


    def test_counties_range_statistic(self):
        """Test to return range index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/range?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "range": 4.3 })
