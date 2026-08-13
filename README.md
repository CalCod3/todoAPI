# Task API

A simple REST API for managing tasks using FastAPI.

## Prerequisites

- Python (v3.7 or higher)
- pip
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todoAPI
```

2. Install dependencies:
```bash
pip install fastapi uvicorn
```

3. Create a `.env` file (if needed) with any required environment variables.

## Running the Project

### Development Mode

Start the development server:
```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

### Production Mode

Start the production server:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - Get API information and available endpoints
- `GET /health` - Health check endpoint
- `GET /tasks` - Retrieve all tasks
- `GET /tasks/{id}` - Retrieve a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## Project Structure

```
todoAPI/
├── src/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   └── index.js
├── tests/
├── .env.example
├── package.json
└── README.md
```

## Testing

Run the test suite:
```bash
npm test
```

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License.
