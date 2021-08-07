from bluesky.callbacks.zmq import Publisher
from bluesky import RunEngine

from databroker import Broker


RE = RunEngine()
publisher = Publisher("localhost:5577")
RE.subscribe(publisher)

db = Broker.named("test")
RE.subscribe(db.insert)
