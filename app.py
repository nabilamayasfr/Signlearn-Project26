from flask import Flask
from routes.web_routes import web

app = Flask(__name__)
app.register_blueprint(web)

if __name__ == "__main__":
    app.run(debug=True)