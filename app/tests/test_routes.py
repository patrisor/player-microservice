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
        # Assert the response is a list
        self.assertIsInstance(data, list)
        # Assert that each item in the response list is a dictionary
        if len(data) > 0:
            self.assertIsInstance(data[0], dict)

    def test_get_specific_player(self):
        """
        Test that the /api/players/<player_id> endpoint returns the correct 
        player data.
        """
        player_id = 'aardsda01'
        response = self.client.get(f'/api/players/{player_id}')
        self.assertEqual(response.status_code, 200)
        # Parse the response data
        data = json.loads(response.data)
        # Assert the response is a dictionary and contains expected keys
        self.assertIsInstance(data, dict)
        self.assertEqual(data['playerID'], player_id)

    def test_get_non_existent_player(self):
        """
        Test that requesting a non-existent player returns a 404 status code.
        """
        player_id = 'nonexistent01'
        response = self.client.get(f'/api/players/{player_id}')
        self.assertEqual(response.status_code, 404)
        # Parse the response data
        data = json.loads(response.data)
        # Assert that an appropriate error message is returned
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Player not found')

if __name__ == '__main__':
    unittest.main()