from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

with open("./schema/key.avsc", "r") as f:
    key_schema = avro.loads(f.read())
with open("./schema/value.avsc", "r") as f:
    value_schema = avro.loads(f.read())


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


avroProducer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'on_delivery': delivery_report,
    'schema.registry.url': 'http://localhost:8081'
}, default_key_schema=key_schema, default_value_schema=value_schema)

for i in range(101, 500):
    key = {"name": f'Nae{i}'}
    value = {"name": f'NaeTest{i}'}
    avroProducer.produce(topic='nae', value=value, key=key)
    avroProducer.flush()
