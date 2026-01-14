# Employee Management System (EMS)

A robust, containerized Employee Management System built with Django and MySQL.

## 🚀 Features

- **Employee Management**: CRUD operations for employee records.
- **Department & Designation**: Organize employees by role.
- **REST API**: Built with Django Rest Framework (DRF).
- **Containerized**: Fully Dockerized for consistent development and deployment.
- **Database**: Production-ready MySQL 8.0 integration.

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Django 5.0
- **API**: Django Rest Framework
- **Database**: MySQL 8.0
- **Containerization**: Docker, Docker Compose
- **Server**: Gunicorn (WSGI)

## 📋 Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [Colima](https://github.com/abiosoft/colima)
- [Git](https://git-scm.com/)

## 🏃‍♂️ Quick Start

1.  **Clone the repository**
    ```bash
    git clone https://github.com/swyam1104/ems_project.git
    cd ems_project
    ```

2.  **Start the application**
    ```bash
    docker-compose up --build
    ```
    *This starts both the Django web server and the MySQL database.*

3.  **Access the Application**
    - Web Interface: [http://localhost:8000](http://localhost:8000)
    - Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

## ⚙️ Configuration

The project uses `docker-compose.yml` for orchestration.
- **Web Service**: Runs on port `8000`.
- **Database Service**: MySQL runs on internal port `3306` (mapped to host `3307` to avoid conflicts).
- **Network**: Services communicate via the custom `ems_network`.

## 🗄️ Database

The project is configured to use **MySQL**.
- Data is persisted in a Docker volume named `db_data`.
- To access the database shell:
  ```bash
  docker-compose exec db mysql -u ems_user -pems_password ems_db
  ```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
