from flask import Flask
from routes.home_router import home_blueprint

app = Flask("fsk-1")
app.config.from_object('settings')
app.register_blueprint(home_blueprint)