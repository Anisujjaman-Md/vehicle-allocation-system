# Vehicle Allocation System - FastAPI & MongoDB

A vehicle allocation system where employees can allocate vehicles for specific days, ensuring no double booking occurs.

## Technologies Used

- **Backend:** FastAPI
- **Database:** MongoDB
- **Containerization:** Docker, Docker Compose

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Running Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/vehicle-allocation-system.git
   cd vehicle-allocation-system
   ```

2. **Run the application:**

   ```bash
   docker-compose up --build
   ```

   Access the application at `http://localhost:8000` and the API documentation at `http://localhost:8000/docs`.

### Stopping the Application

To stop the application, run:

```bash
docker-compose down
```

## Deployment

1. **Build and tag the Docker image:**

   ```bash
   docker build -t your-dockerhub-username/vehicle-allocation-system .
   ```

2. **Push to Docker Hub:**

   ```bash
   docker push your-dockerhub-username/vehicle-allocation-system
   ```

3. **Deploy on any cloud service supporting Docker,** like AWS ECS, GCP, or Azure, following their specific deployment guidelines.

### Notes

- Ensure to manage environment variables for sensitive data.
- Set up logging and monitoring for production environments.
