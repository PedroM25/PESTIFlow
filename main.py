""" Module from where program execution starts.
This module will spawn each UCs UI, depending on the subparser passed as an argument."""

import argparse
import os.path

from view.cicids2018_extraction_ui import CICIDS2018ExtractionUI
from view.graylog_extraction_ui import GraylogExtractionUI
from view.pcap_extraction_ui import PcapExtractionUI
from view.retourdeflamme_extraction_ui import RetourDeFlammeExtractionUI


def _check_file_exists(path: str):

    seperators = ["/", "\\"]
    for sep in seperators:
        split_path = path.split(sep)
        if len(split_path) > 1:
            if not os.path.isdir(sep.join(split_path[:-1])):
                raise argparse.ArgumentTypeError(f"\"{path}\" does not lead to a valid file.")
            return path
    raise argparse.ArgumentTypeError(f"\"{path}\" does not lead to a valid file.")


def pcap(args):
    PcapExtractionUI("PCAP feature extraction", args.bi).display(args.input, args.output, args.groundtruth,
                                                                 args.timeout)


def retourdeflamme(args):
    RetourDeFlammeExtractionUI("\"Retour de Flamme\" feature extraction").display(args.input, args.output,
                                                                                  args.groundtruth)


def graylog(args):
    GraylogExtractionUI("Graylog feature extraction").display(args.input, args.output, args.groundtruth)


def cicids2018(args):
    CICIDS2018ExtractionUI("CICIDS 2018 feature extraction").display(args.input, args.output)


parser = argparse.ArgumentParser(description="PESTIFlow app created by Pedro Ribeiro (1160779@isep.ipp.pt)")

# POSITIONAL ARGUMENTS

# Positional argument 1
parser.add_argument("input", help="Path to the file from where features will be extracted.",
                    type=_check_file_exists)

# Positional argument 2
parser.add_argument("output", help="Path to the file where calculated flows will be stored."
                                   " File will be in CSV format.", type=_check_file_exists)

# PARENT PARSERS

# Parent parser of all file formats which support ground truth being fed into them (or not)
gt_parser = argparse.ArgumentParser(add_help=False)
gt_parser.add_argument("-gt", "--groundtruth", help="Path to the file containing ground truth information used to label"
                                                    " the flows. File must be in CSV format.",
                       type=_check_file_exists)

# Parent parser of all file formats which support obtaining bidirectional flows from them
bi_parser = argparse.ArgumentParser(add_help=False)
bi_parser.add_argument("-bi", action="store_true", default=False,
                       help="Indicates that bidirectional flows should be constructed from the input data, "
                            "instead of the default unidirectional flows.")

# SUBPARSERS
subparsers = parser.add_subparsers(title="Supported file formats",
                                   help="Supported file formats for feature extraction.")

# PCAP subparser
pcap_parser = subparsers.add_parser("pcap", help="Input file follows the tcpdump format, also known as the \"pcap\" "
                                                 "format.", parents=[gt_parser, bi_parser])
pcap_parser.add_argument("--timeout", help="Defines the maximum time interval, in seconds, between two packets of the "
                                           "same flow. If the time arrival time difference between the current packet "
                                           "and the last received packet of the flow to which the current packet "
                                           "belongs to, is superior to this value, a new flow is created from the "
                                           "received packet. Default value is 15s.", type=int, default=15)
pcap_parser.set_defaults(func=pcap)

# retourdeflame subparser
retourdeflame_parser = subparsers.add_parser("retourdeflamme",
                                             help="Input file follows the format of the \"RetourDeFlamme\" files "
                                                  "provided by Airbus.", parents=[gt_parser])
retourdeflame_parser.set_defaults(func=retourdeflamme)

# graylog subparser
graylog_parser = subparsers.add_parser("graylog",
                                       help="Input file follows the format of the Graylog files "
                                            "provided by Airbus.", parents=[gt_parser])
graylog_parser.set_defaults(func=graylog)

# CICIDS 2018 subparser
cicids2018_parser = subparsers.add_parser("cicids2018", help="Input file corresponds to one of the files available in "
                                                             "the CICIDS 2018 dataset.")
cicids2018_parser.set_defaults(func=cicids2018)

if __name__ == '__main__':
    arguments = parser.parse_args()
    arguments.func(arguments)
