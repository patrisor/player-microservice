import sqlite3
from flask import jsonify
from app.config import DB_PATH

def register_routes(app, cache):
    """
    Register the REST API routes to the Flask application.

    Args:
        app (Flask): The Flask application instance where routes will be 
                     registered.
    """

    @app.route('/api/players', methods=['GET'])
    @cache.cached(timeout=60) # Cache the result of the method for 60 seconds
    def get_players():
        """
        Endpoint to retrieve all players.

        Returns:
            JSON Response: A JSON list containing all players' data.
        """
        # Connect to SQLite and fetch all players
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players")
            players = cursor.fetchall()
            # Get column names to construct response dictionaries
            column_names = [
                description[0]
                for description
                in cursor.description
            ]
            # Combine column names with player data to create a dictionary
            players_list = [
                dict(zip(column_names, player)) for player in players
            ]
        # Return the list as JSON with HTTP status code 200 (OK)
        return jsonify(players_list), 200

    @app.route('/api/players/<string:player_id>', methods=['GET'])
    @cache.memoize(timeout=60) # Memoize the result of the method for 60 seconds
    def get_player(player_id):
        """
        Endpoint to retrieve a specific player by their ID.

        Args:
            player_id (str): The unique ID of the player.

        Returns:
            JSON Response: A JSON object containing the player's data or an 
                           error message.
        """
        # Connect to SQLite and fetch player by ID
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM players WHERE playerID = ?", (player_id,)
            )
            player = cursor.fetchone()
            if player:
                # Get column names from the cursor description
                column_names = [
                    description[0]
                    for description 
                    in cursor.description
                ]
                # Combine column names with player data to create a dictionary
                player_data = dict(zip(column_names, player))
                return jsonify(player_data), 200
            else:
                # Return a 404 error if no player with the given ID is found
                return jsonify({"error": "Player not found"}), 404