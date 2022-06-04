import app
import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/api/v1/county"

    def test_all_counties(self):
        """Test to return count of all counties in db"""
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)

    def test_county_show(self):
        """Test to return county by its zip"""
        response = requests.get(self.URL + "?10001")
        self.assertEqual(response.status_code, 200)

    def test_counties_mean_statistic(self):
        """Test to return mean index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/mean?1001&10003&10005")
        self.assertEqual(response.status_code, 200)

    def test_counties_median_statistic(self):
        """Test to return median index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/median?1001&10003&10005")
        self.assertEqual(response.status_code, 200)

    def test_counties_stdev_statistic(self):
        """Test to return (sample) standard deviation index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/stdev?1001&10003&10005")
        self.assertEqual(response.status_code, 200)

    def test_counties_range_statistic(self):
        """Test to return range index for given counties"""
        response = requests.get(self.URL + "/happiness_stats/range?1001&10003&10005")
        self.assertEqual(response.status_code, 200)
