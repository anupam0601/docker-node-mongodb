import json
from collections import OrderedDict
from pprint import pprint

with open('log.json') as data_file:
    # orderedDict to maintain the same order of json in python dictionary
    data = json.load(data_file, object_pairs_hook=OrderedDict)


if __name__ == '__main__':

    print json.dumps(data, indent=4)

    print data["log_stat"]
