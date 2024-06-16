# src/main.py
from database import init_db

if __name__ == "__main__":
    init_db()
    print("Database initialized!")
# src/main.py
from cli.cli import cli

if __name__ == "__main__":
    cli()
