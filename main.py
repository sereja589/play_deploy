import time
from flask import Flask, json


api = Flask(__name__)


@api.route('/time', methods=['GET'])
def get_time():
    return json.dumps({
        'time': int(time.time())
    })


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
