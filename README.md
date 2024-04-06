# API_Service

API_Service is a robust application designed to provide specific data to users via RESTful endpoints. This service, exemplified through a book information provision API, allows for interactions such as fetching author details, publication years, genres, and reviews of books.

## Overview

The API_Service leverages Django with Django REST framework for its backend, employing PostgreSQL as its database. It is containerized with Docker, ensuring easy deployment and scalability. The application architecture emphasizes RESTful API principles, incorporating features like user authentication, rate limiting, data filtering, and pagination for efficient data management.

## Features

- **RESTful API Endpoints:** Utilizes GET, POST, PUT, and DELETE methods to interact with book data.
- **User Authentication:** Secures API access through token-based authentication.
- **Rate Limiting:** Implements rate limiting to prevent service abuse.
- **Data Filtering and Pagination:** Efficiently manages large sets of data.
- **Logging and Monitoring:** Tracks API usage and errors for maintenance and optimization.

## Getting started

### Requirements

- Django>=3.0,<4.0
- djangorestframework
- django-filter
- psycopg2-binary>=2.8
- djangorestframework-simplejwt>=4.6.0

### Quickstart

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the PostgreSQL database and update the `DATABASES` configuration in `settings.py`.
4. Run migrations with `./manage.py migrate` to set up your database schema.
5. Start the server using `./manage.py runserver`.
6. Explore the API endpoints as described in the documentation.

### License

Copyright (c) 2024.