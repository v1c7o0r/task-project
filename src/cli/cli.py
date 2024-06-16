# src/cli/cli.py
import click
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import User, Project, Task

# Database session context manager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@click.group()
def cli():
    """Task and Project Management CLI"""
    pass

@cli.command()
@click.option('--name', prompt='User name', help='The name of the user.')
@click.option('--email', prompt='User email', help='The email of the user.')
def create_user(name, email):
    """Create a new user"""
    db: Session = next(get_db())
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    click.echo(f'User {name} created!')

@cli.command()
@click.option('--user-id', prompt='User ID', help='The ID of the user to delete.')
def delete_user(user_id):
    """Delete a user"""
    db: Session = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        click.echo(f'User {user.name} deleted!')
    else:
        click.echo('User not found!')

@cli.command()
def list_users():
    """List all users"""
    db: Session = next(get_db())
    users = db.query(User).all()
    for user in users:
        click.echo(f'{user.id}: {user.name} ({user.email})')

# Add more CLI commands for projects and tasks similarly...

if __name__ == '__main__':
    cli()
