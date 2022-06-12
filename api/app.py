from flask import Flask
from flask_cors import CORS
from db import DB
from resources.user import create_user
from security import login
from flask_jwt_extended import JWTManager

# Create a new Flask application
app = Flask(__name__)
app.debug = True

# Enable cors on the server
CORS(app)

# Register the JWT manager
app.config["JWT_SECRET_KEY"] = "super-duper-secret"
jwt = JWTManager(app)

# ============================ Routes ============================

# JWT routes
app.add_url_rule("/users", None, create_user, methods=["POST"])
app.add_url_rule("/auth", None, login, methods=["POST"])

# Start app
if __name__ == '__main__':
    DB.create()
    app.run()