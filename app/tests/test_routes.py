import unittest
import json
from flask import Flask
from app.main import create_app

class PlayerServiceTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the Flask application and test client.
        This function is called before each test.
        """
        # Create an instance of the Flask app
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.testing = True

    def test_get_all_players(self):
        """
        Test that the /api/players endpoint returns a list of players with 
        status code 200.
        """
        response = self.client.get('/api/players')
        self.assertEqual(response.status_code, 200)
        # Parse the response data
        data = json.loads(response.data)
        # Assert the response
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)

    def test_get_specific_player(self):
        """
        Test that the /api/players/<player_id> endpoint returns the correct 
        player data.
        """
        player_id = "aardsda01"
        expected_player = {
            "playerID": "aardsda01",
            "birthYear": 1981,
            "birthMonth": 12,
            "birthDay": 27,
            "birthCountry": "USA",
            "birthState": "CO",
            "birthCity": "Denver",
            "deathYear": None,
            "deathMonth": None,
            "deathDay": None,
            "deathCountry": None,
            "deathState": None,
            "deathCity": None,
            "nameFirst": "David",
            "nameLast": "Aardsma",
            "nameGiven": "David Allan",
            "weight": 215,
            "height": 75,
            "bats": "R",
            "throws": "R",
            "debut": "2004-04-06",
            "finalGame": "2015-08-23",
            "retroID": "aardd001",
            "bbrefID": "aardsda01"
        }
        response = self.client.get(f'/api/players/{player_id}')
        self.assertEqual(response.status_code, 200)
        # Verify that every field matches the expected values
        player_data = json.loads(response.data)
        self.assertEqual(player_data, expected_player)

    def test_get_non_existent_player(self):
        """
        Test that requesting a non-existent player returns a 404 status code.
        """
        player_id = 'nonexistent01'
        # Assert that the appropriate status code is returned
        response = self.client.get(f'/api/players/{player_id}')
        self.assertEqual(response.status_code, 404)
        # Assert that an appropriate error message is returned
        error_message = json.loads(response.data)
        self.assertEqual(error_message, {"error": "Player not found"})

if __name__ == '__main__':
    unittest.main()