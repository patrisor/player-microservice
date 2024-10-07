# Player Microservice

## Overview
The Player Microservice is a simple REST API built using Flask, which serves player data from a CSV file (`Player.csv`). It exposes two endpoints:
- `GET /api/players`: Fetches a list of all players.
- `GET /api/players/<player_id>`: Fetches details of a specific player by their unique ID.

## Features
- **List All Players**: Retrieve a list of all players with relevant details.
- **Get Player by ID**: Retrieve information for a specific player using their unique identifier.

## Setup Instructions

### 1. Clone the Repository
Start by cloning the repository to your local machine:

```sh
git clone <repository-url>
cd player_microservice
```

### 2. Create and Activate a Virtual Environment (Recommended)
It is recommended to use a virtual environment to keep dependencies isolated:

```sh
python -m venv .venv  # Create virtual environment
source .venv/bin/activate  # Activate (Linux/macOS)
.venv\Scripts\activate  # Activate (Windows)
```

### 3. Install Dependencies
Install the required packages listed in `requirements.txt`:

```sh
pip install -r requirements.txt
```

This command installs the following main dependencies:
- **Flask**: A lightweight web framework for building REST APIs.
- **pandas**: A powerful library for data manipulation, used to read and process the CSV file.

### 4. Running the Server
To start the Flask server and make the API available:

```sh
python -m app.main
```

- By default, the server runs on `http://0.0.0.0:5000`.
- The following endpoints are available:
  - **`GET /api/players`**: Returns all player data.
  - **`GET /api/players/<player_id>`**: Returns the details of the player with the given `player_id`.

### 5. Example Requests

- **Fetch All Players**:

  ```sh
  curl http://localhost:5000/api/players
  ```
  
- **Fetch a Specific Player**:

  ```sh
  curl http://localhost:5000/api/players/aardsda01
  ```

  Replace `aardsda01` with the desired player ID.

### 6. Running Unit Tests
Unit tests are provided to validate the core functionality of the microservice.

To run the tests:

```sh
python -m unittest discover -s app/tests
```

This will:
- Test the `/api/players` endpoint to ensure it returns all players.
- Test the `/api/players/<player_id>` endpoint to verify it returns the correct player or a 404 error if the player does not exist.

### 7. How to Customize
- **Modify `Player.csv`**: You can update the `Player.csv` file in the `data/` directory to include additional players or modify the data.
- **Add More Features**: Extend the `routes.py` to add more functionality, such as adding new players, updating details, or deleting players.

## Technologies Used
- **Python**: Primary language for building the microservice.
- **Flask**: Lightweight web framework for RESTful APIs.
- **pandas**: Library used to read and manipulate player data from a CSV file.

## License
This project is licensed under the MIT License.
