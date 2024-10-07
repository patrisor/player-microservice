import os
import json
import pandas as pd
from flask import jsonify

# Load the CSV file at the start to keep data available throughout the service 
# runtime
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/Player.csv')
players_df = pd.read_csv(DATA_PATH)

def register_routes(app):
    """
    Register the REST API routes to the Flask application.

    Args:
        app (Flask): The Flask application instance where routes will be 
                     registered.
    """

    @app.route('/api/players', methods=['GET'])
    def get_players():
        """
        Endpoint to retrieve all players.

        Returns:
            JSON Response: A JSON list containing all players' data.
        """
        # Convert the players DataFrame to a list of dictionaries
        players = players_df.to_dict(orient='records')
        # Return the list as JSON with HTTP status code 200 (OK)
        return jsonify(players), 200

    @app.route('/api/players/<string:player_id>', methods=['GET'])
    def get_player(player_id):
        """
        Endpoint to retrieve a specific player by their ID.

        Args:
            player_id (str): The unique ID of the player.

        Returns:
            JSON Response: A JSON object containing the player's data or an 
                           error message.
        """
        # Filter the DataFrame for the row with the given player ID
        player = players_df[players_df['playerID'] == player_id]
        if not player.empty:
            # If the player exists, convert the first (and only) row to a 
            # dictionary and return it
            return jsonify(player.iloc[0].to_dict()), 200
        else:
            # Return a 404 error if no player with the given ID is found
            return jsonify({"error": "Player not found"}), 404