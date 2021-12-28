import re

from model.services import io_service

PROTO_TO_IANA_NO = {"tcp": 6, "udp": 17}
DELIM = ","  # DELIM should be received as input
NOT_AVAILABLE = "n.a."

ATTACK = "Attack"
NORMAL = "Normal"
ATTACK_RESPONSE = "AttackResponse"


def identify_unique_keys(entry, dictionary):
    for k in entry.keys():
        if k not in dictionary:
            dictionary[k] = {}
        if isinstance(entry[k], dict):
            dictionary[k] = identify_unique_keys(entry[k], dictionary[k])
    return dictionary


def show_key_structure(str_before, dictionary):
    for k in dictionary:
        print(str_before + k, flush=True)
        if isinstance(dictionary[k], dict) and dictionary[k]:
            show_key_structure(str_before + "\t", dictionary[k])


def generate_attribute_code_from_csv_headers(file_path):
    i = 0
    for header in next(io_service.read_lines_csv_file(file_path, DELIM)):
        print("_" + re.sub("[^a-zA-Z0-9]", "_", header).upper() + " = " + str(i))
        i += 1
