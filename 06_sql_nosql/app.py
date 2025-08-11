from flask import Flask
from routes.mysql_routes import mysql_bp
from routes.nosql_routes import nosql_bp  # You’d create this similarly

app = Flask(__name__)

app.register_blueprint(mysql_bp, url_prefix='/mysql')
app.register_blueprint(nosql_bp, url_prefix='/nosql')

if __name__ == '__main__':
    app.run(debug=True)
