import json
import time
import datetime
import logging

from flask import (
    Flask,
    request,
    jsonify 
)

from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError

# - default kafka topic to write to
topic_name = 'stock-analyzer'

# - default kafka broker location
kafka_broker = '54.198.167.134:9092'

producer = KafkaProducer(
        bootstrap_servers=kafka_broker
)

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-producer')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_stock():
    content = request.json
    print content
    if not content:
       return jsonify({
            'error': 'didn\'t get data'
        }), 400
    else:
        producer.send(topic=topic_name, value=content.encode('utf-8'), timestamp_ms=time.time())
        logger.info('Sent data of web log to Kafka')
	return jsonify({'info': 'Accept'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
