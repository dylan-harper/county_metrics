import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/api/v1/county"

#happy path testing
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
        response = requests.get(self.URL + "/happiness_stats/median?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "median": 100.6 })

    def test_counties_stdev_statistic(self):
        """Test to return (sample) standard deviation for given counties' indexes"""
        response = requests.get(self.URL + "/happiness_stats/stdev?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "stdev": 2.35 })

    def test_counties_range_statistic(self):
        """Test to return range for given counties indexes"""
        response = requests.get(self.URL + "/happiness_stats/range?10001&10003&10005")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "range": 4.3 })

#sad path testing
    def test_for_entry_not_in_db(self):
        """Test to ensure error handling for incorrect counties"""
        response = requests.get(self.URL + "/87953")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), { "error": "87953 is not included in the dataset"})

    def test_for_incorrect_statistic_action(self):
        """Test to ensure users cannot enter incorrect actions/statistics"""
        response = requests.get(self.URL + "/happiness_stats/mud?10001&10003&10005")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), { "error": "Invalid statistic, choose one: [mean, median, stdev, range]" })

    def test_for_not_enough_counties_in_query(self):
        """Test to ensure users are sending over more than one county for each query"""
        response = requests.get(self.URL + "/happiness_stats/median?10001")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), { "error": "Must include more than one county" })

    def test_for_valid_counties(self):
        """Test for valid county entries when calculating stats"""
        response = requests.get(self.URL + "/happiness_stats/median?10001&10003&789456")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), { "error": "789456 is not included in the dataset" })
