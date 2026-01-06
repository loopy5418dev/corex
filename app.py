from flask import Flask
from routes import register_routes
from errors import errors

app = Flask(__name__)

register_routes(app)
app.register_blueprint(errors)

if __name__ == "__main__":
    app.run(debug=True)