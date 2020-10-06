from flask import Flask, send_from_directory
from flask_restful import Resource, Api, request

from datetime import datetime
import psycopg2
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
api = Api(app)


def get_sales(fromDt, toDt):
    """ query data from the sales table """
    conn = None
    try:
        # params = config()
        params = {
            'host': os.environ.get('POSTGRES_HOST'),
            'database': os.environ.get('POSTGRES_DB'),
            'user': os.environ.get('POSTGRES_USER'),
            'password': os.environ.get('POSTGRES_PASSWORD')
        }
        print(params)

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT gender, count(*) FROM sales WHERE date BETWEEN %s AND %s GROUP BY gender",
                       (fromDt, toDt))

        result = {'names': [], 'sizes': []}
        row = cursor.fetchone()
        while row is not None:
            print(row)
            result['names'].append(row[0])
            result['sizes'].append(row[1])
            row = cursor.fetchone()

        cursor.close()

        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


class HelloPloomes(Resource):
    def get(self):
        args = request.args

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        try:
            data = get_sales(fromDt=args['fromDt'], toDt=args['toDt'])
            print(data)
            labels = data['names']
            sizes = data['sizes']

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.axis('equal')
            now = datetime.now().strftime('%H%M%S')

            filename = '{}.png'.format(now)
            fig1.savefig(filename)

            """Download a file."""
            return send_from_directory('../', filename, as_attachment=False)
        except FileNotFoundError:
            abort(404)

        return {'message': filename}


api.add_resource(HelloPloomes, '/sales-gender')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
