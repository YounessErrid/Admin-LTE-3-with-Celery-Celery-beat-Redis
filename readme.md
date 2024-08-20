Admin-LTE-3-with-Celery-Celery-beat-Redis
Project Overview
This project integrates AdminLTE 3, Celery, Celery Beat, and Redis to create a robust and scalable web application. AdminLTE 3 provides a modern admin dashboard UI, while Celery and Celery Beat handle asynchronous tasks and periodic tasks, respectively, with Redis used as the message broker. Additionally, Mailtrap is integrated for email testing.

Features
AdminLTE 3: A fully responsive admin dashboard template built on Bootstrap 4.
Celery: Asynchronous task queue/job queue based on distributed message passing.
Celery Beat: Scheduler for periodic tasks in Celery.
Redis: In-memory data structure store used as a message broker for Celery.
Mailtrap: Email testing tool for capturing and inspecting emails sent by your application.
Installation
Prerequisites
Docker
Docker Compose
Setting Up the Project
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/Admin-LTE-3-with-Celery-Celery-beat-Redis.git
cd Admin-LTE-3-with-Celery-Celery-beat-Redis
Build and Start the Docker Containers

bash
Copy code
docker-compose up --build
This command will build the Docker images and start the containers for your Django application, Redis, and any other services defined in the docker-compose.yml file.

Create and Apply Database Migrations

Open a new terminal and run:

bash
Copy code
docker-compose exec web python manage.py migrate
Collect Static Files

bash
Copy code
docker-compose exec web python manage.py collectstatic --noinput
Configure Environment Variables

Create a .env file in the root directory of your project with the following content:

env
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# Mailtrap settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.mailtrap.io
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_mailtrap_username
EMAIL_HOST_PASSWORD=your_mailtrap_password
Replace your_mailtrap_username and your_mailtrap_password with your Mailtrap credentials.

Running the Application
Start the Application

bash
Copy code
docker-compose up
This will start all services defined in your docker-compose.yml file. By default, the application will be accessible at http://localhost:8000.

Start Celery Worker

Open a new terminal and run:

bash
Copy code
docker-compose run web celery -A your_project_name worker --loglevel=info
Start Celery Beat Scheduler

Open another terminal and run:

bash
Copy code
docker-compose run web celery -A your_project_name beat --loglevel=info
Email Testing with Mailtrap
Mailtrap allows you to test email sending functionality without sending emails to real users. Use the provided Mailtrap credentials in your .env file to capture and inspect emails sent by your application.

Docker Compose File
Here's a sample docker-compose.yml file for your project:

yaml
Copy code
version: '3.8'

services:
  web:
    image: your_django_image
    container_name: web
    command: gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - redis
    env_file:
      - .env

  redis:
    image: redis:latest
    container_name: redis

  celery:
    image: your_django_image
    container_name: celery
    command: celery -A your_project_name worker --loglevel=info
    volumes:
      - .:/app
    depends_on:
      - redis
    env_file:
      - .env

  celery-beat:
    image: your_django_image
    container_name: celery-beat
    command: celery -A your_project_name beat --loglevel=info
    volumes:
      - .:/app
    depends_on:
      - redis
    env_file:
      - .env
Usage
Access the AdminLTE 3 dashboard at http://localhost:8000/admin/.
Configure and manage your asynchronous and periodic tasks through Celery.
Test email functionality using Mailtrap by sending emails through your application.
Contributing
Feel free to contribute to this project by submitting pull requests or opening issues. Please follow the code of conduct and guidelines for contributions.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
AdminLTE 3: AdminLTE
Celery: Celery
Redis: Redis
Mailtrap: Mailtrap
