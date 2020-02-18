import os
import json
import yaml
import sys

config_file = sys.argv[1]

in_fh = open(config_file, "r")

config_dict = dict()
valid_json = True
valid_yaml = True

try:
    config_dict = json.load(in_fh)
except:
    print("Error trying to load the config file in JSON format")
    valid_json = False

try:
    config_dict = yaml.safe_load(in_fh)
except:
    print ("Error trying to load the config file in YAML format")
    valid_yaml = False

in_fh.close()

if not valid_yaml and not valid_json:
    print ("The config file is neither JSON or YAML")
    sys.exit(1)
