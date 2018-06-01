from models.models import (Book, Author, db)

def migrate():
    db.create_all()
