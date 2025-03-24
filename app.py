from flask import Flask
from routes.routes import kite_routes  
from flask_cors import CORS  


app = Flask(__name__)
CORS(app, origins=["http://localhost:4200","https://algo-trading-ffb.netlify.app"])  


@app.route('/')
def home():
    return "Hello, Flask!"

# Register Blueprint with a prefix
app.register_blueprint(kite_routes, url_prefix='/kite')

if __name__ == '__main__':
    app.run(debug=True)
