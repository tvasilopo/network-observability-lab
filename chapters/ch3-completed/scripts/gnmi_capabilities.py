from pygnmi.client import gNMIclient
import json


with gNMIclient(
    target=("198.51.100.11", 50051), username="netobs", password="netobs123", insecure=True
) as gc:
    result = gc.capabilities()

print(json.dumps(result, indent=True))
