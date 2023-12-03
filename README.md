
# Daraz Price Tracker

Daraz Price Tracker is a Flask web app that allows users to track and visualize the price history of products on Daraz.com.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Clone the Repository](#clone-the-repository)
- [Setup Virtual Environment](#setup-virtual-environment)
- [Install Dependencies](#install-dependencies)
- [Database Setup](#database-setup)
- [Run the Application](#run-the-application)
- [Access the Application](#access-the-application)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following software installed on your machine:

- Python 3.x
- Git

## Clone the Repository

Open a terminal (Command Prompt on Windows, Terminal on macOS) and run the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of your repository.

## Setup Virtual Environment

Navigate to the project directory:

```bash
cd price_tracker
```

Create a virtual environment:

- On Windows:

  ```bash
  python -m venv venv
  ```

- On macOS/Linux:

  ```bash
  python3 -m venv venv
  ```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

## Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

Initialize and migrate the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Run the Application

Run the Flask application:

```bash
python run.py
```

## Access the Application

Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Contributing

If you'd like to contribute to this project, please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

