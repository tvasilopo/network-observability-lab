from pygnmi.client import gNMIclient
import json

paths = ['openconfig:interfaces']

with gNMIclient(
    target=("198.51.100.11", 50051),
    username="netobs",
    password="netobs123",
    insecure=True,
    skip_verify=True,
    timeout = 180
) as gc:

    result = gc.get(path=paths, encoding='json')

print(json.dumps(
    result["notification"][0]["update"][0]["val"]["openconfig-interfaces:interface"][0]["state"],
    indent=True
))
