from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloPloomes(Resource):
    def get(self):
        return {'message': 'Hello ploomes! :D'}


api.add_resource(HelloPloomes, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
