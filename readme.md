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
   git clone https://github.com/yourusername/Admin-LTE-3-with-Celery-Celery-beat-Redis.git
   cd Admin-LTE-3-with-Celery-Celery-beat-Redis
