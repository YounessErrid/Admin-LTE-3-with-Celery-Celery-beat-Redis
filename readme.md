
# Admin-LTE-3-with-Celery-Celery-beat-Redis

## Project Overview

This project integrates AdminLTE 3, Celery, Celery Beat, and Redis to create a robust and scalable web application. AdminLTE 3 provides a modern admin dashboard UI, while Celery and Celery Beat handle asynchronous tasks and periodic tasks, respectively, with Redis used as the message broker. Additionally, Mailtrap is integrated for email testing.

## Features

- **AdminLTE 3**: A fully responsive admin dashboard template built on Bootstrap 4.
- **Celery**: Asynchronous task queue/job queue based on distributed message passing.
- **Celery Beat**: Scheduler for periodic tasks in Celery.
- **Redis**: In-memory data structure store used as a message broker for Celery.
- **Mailtrap**: Email testing tool for capturing and inspecting emails sent by your application.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Setting Up the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/youness-errid2/Admin-LTE-3-with-Celery-Celery-beat-Redis.git
   cd Admin-LTE-3-with-Celery-Celery-beat-Redis
2.   **Build and Start the Docker Containers**
    

    `docker-compose up --build` 
    
    # This command will build the Docker images and start the containers for your Django application, Redis, and any other services defined in the `docker-compose.yml` file.
    
3.   **Create and Apply Database Migrations**
    
    # Open a new terminal and run:
    `docker-compose exec web python manage.py migrate` 
    
4.   **Collect Static Files**
    
    `docker-compose exec web python manage.py collectstatic --noinput` 
    
5.   **Configure Environment Variables**
    
    # Create a `.env` file in the root directory of your project with the following content:
    
    SECRET_KEY=your_secret_key
    DEBUG=True
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    
    # Mailtrap settings
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.mailtrap.io
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your_mailtrap_username`
    2.  Replace `your_mailtrap_username` and `your_mailtrap_password` with your Mailtrap credentials.

### Usage

-   Access the AdminLTE 3 dashboard at `http://localhost:8000/admin/`.
-   Configure and manage your asynchronous and periodic tasks through Celery.
-   Test email functionality using Mailtrap by sending emails through your application.


### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements

-   **AdminLTE 3**: [AdminLTE](https://adminlte.io/)
-   **Celery**: Celery
-   **Redis**: [Redis](https://redis.io/)
-   **Mailtrap**: [Mailtrap](https://mailtrap.io/)
