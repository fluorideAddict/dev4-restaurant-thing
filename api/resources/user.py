from os import access
from flask import request, jsonify
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from db import DB
from flask_jwt_extended import(
    jwt_required,
    create_access_token,
    get_jwt_identity
)

def create_user():
    # Parse all arguments for validity
    args = request.get_json()

    # Make the insert query with parameters
    qry = """
    INSERT INTO
        `users`
            (`email`, `password`, `firstname`, `lastname`)
        VALUES
            (:email, :password, :firstname, :lastname)
    """

    # Hash the password before inserting
    args["password"] = generate_password_hash(args["password"])

    # Insert the user into the database
    id = DB.insert(qry, args)

    # Return a message and the user id
    return {"message": "success", "id": id}, 201