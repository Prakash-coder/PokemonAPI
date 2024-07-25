# Pokemon API

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone <repo_url>
    cd pokemon-api
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Setup PostgreSQL database** and update `.env` file with the connection details:
    ```dotenv
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/pokemon_db
    ```

5. **Run Alembic migrations**:
    ```sh
    alembic upgrade head
    ```

6. **Fetch and store Pokémon data**:
    ```sh
    python fetch_and_store_pokemons.py
    ```

7. **Run the FastAPI application**:
    ```sh
    uvicorn app.main:app --reload
    ```

8. **Access the HTML file**:
    Open your web browser and navigate to `http://localhost:8000/`.

## API Endpoints

### `GET /api/v1/pokemons`

Retrieve a list of Pokémon with optional filtering by name and type.

**Request Parameters**:
- `name` (optional): Keyword to filter Pokémon by name.
- `type` (optional): Keyword to filter Pokémon by type.

**Response**:
- List of Pokémon with their `name`, `image`, and `type`.

**Example Requests**:
- Retrieve all Pokémon:
    ```sh
    curl -X GET "http://localhost:8000/api/v1/pokemons"
    ```
- Filter Pokémon by name:
    ```sh
    curl -X GET "http://localhost:8000/api/v1/pokemons?name=pikachu"
    ```
- Filter Pokémon by type:
    ```sh
    curl -X GET "http://localhost:8000/api/v1/pokemons?type=electric"
    ```
- Filter Pokémon by name and type:
    ```sh
    curl -X GET "http://localhost:8000/api/v1/pokemons?name=pika&type=electric"
    ```

### `POST /api/v1/pokemons`

Add a new Pokémon.

**Request Body**:
- `name` (required): Name of the Pokémon.
- `image` (required): URL of the Pokémon's image.
- `type` (required): Type(s) of the Pokémon.

**Response**:
- The newly created Pokémon with its `id`, `name`, `image`, and `type`.

**Example Request**:
```sh
curl -X POST "http://localhost:8000/api/v1/pokemons" -H "Content-Type: application/json" -d '{"name": "Bulbasaur", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png", "type": "grass, poison"}'
