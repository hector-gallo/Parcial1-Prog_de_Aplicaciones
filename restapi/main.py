from flask import Flask
from flask_restful import Api
from resource.store import store


app = Flask(__name__)
api = Api(app)

api.add_resource(store, "/store/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=2351)
