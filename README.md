# API_Service

API_Service is a Django project that provides a RESTful API to manage a library system. It supports operations for managing books, authors, and genres, allowing users to add, retrieve, update, and delete records. The project uses Django REST Framework to build the API endpoints and PostgreSQL as the database backend.

## Overview

This project follows a traditional Django project structure with a focus on RESTful API design. It leverages Django REST Framework for creating API views and serializers and uses Django's ORM for database interactions. The application is containerized using Docker, facilitating easy setup and deployment.

## Features

- CRUD operations for books, authors, and genres
- User authentication and authorization
- Search and filtering capabilities
- Containerized setup with Docker and docker-compose

## Getting started

### Requirements

- Docker
- docker-compose

### Quickstart

1. Clone the repository:
   ```bash
   git clone https://example.com/API_Service.git
   cd API_Service
   ```
2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```
3. Access the API at `http://localhost:8001/`

### License

Copyright (c) 2024.