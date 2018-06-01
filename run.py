from app import app
import db

db.migrate()

app.run()