from flask import Flask, jsonify

app = Flask(__name__)

airport_database = {
    'EFHK': {'Name': 'Helsinki Vantaa Airport', 'Municipality': 'Helsinki'},

}

@app.route('/kentta/<icao>', methods=['GET'])
def get_airport_info(icao):
    icao_code = icao.upper()

    if icao_code in airport_database:
        airport_info = {
            'ICAO': icao_code,
            'Name': airport_database[icao_code]['Name'],
            'Municipality': airport_database[icao_code]['Municipality'],
        }
        return jsonify(airport_info)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)