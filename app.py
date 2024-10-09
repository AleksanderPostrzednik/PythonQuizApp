from flask import Flask
from app import create_app, db
from app.routes import main

app = create_app()

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)