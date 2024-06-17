# phase3-project
# Task and Project Management Tool

## Description

The Task and Project Management Tool is a Python CLI application designed to help users manage tasks and projects. It provides functionality to track deadlines, priorities, and project progress using a command-line interface. The application uses SQLAlchemy for ORM and follows best practices in CLI design.

## Features

- **User Management**: Create, delete, and list users.
- **Project Management**: Create, delete, and list projects, assign projects to users.
- **Task Management**: Create, delete, and list tasks within a project, assign tasks to projects.
- **Task Status and Priority Management**: Update task status and priority.
- **Reporting**: Generate reports on project progress and overdue tasks.

## Installation

### Prerequisites

- Python 3.8+
- Pipenv (for managing the virtual environment and dependencies)

### Steps

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd task_project_manager
    ```

2. **Install Pipenv** (if not already installed):
    ```bash
    pip install pipenv
    ```

3. **Install dependencies**:
    ```bash
    pipenv install
    ```

4. **Initialize the database**:
    ```bash
    pipenv run python src/main.py
    ```

## Usage

### Running the Application

To start the CLI application, run:
```bash
pipenv run python src/main.py
