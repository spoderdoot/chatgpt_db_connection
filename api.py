from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

PORT = 5000

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(port=PORT, debug=True)