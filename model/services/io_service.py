import csv
import json
from pathlib import Path

from scapy.sendrecv import sniff


class IOService:

    def write_feature_vectors_to_csv(self, file_path, fvl):
        """ list_fv is a FeatureVectorList object
        """
        with open(file_path, mode="w", newline="", encoding="utf-8") as output_file:
            output_writer = csv.writer(output_file, delimiter=",")
            i = 1
            for fv in fvl:
                if i == 1:
                    output_writer.writerow(fv.all_variables().keys())
                output_writer.writerow(fv.all_variables().values())
                i += 1
        return Path(file_path).stat().st_size

    def read_pcap(self, file_path):
        """Scapy alternatives:
         rdpcap (reads pcap in its entirety);
         PcapReader (yields packets) https://stackoverflow.com/questions/44440738/iterate-through-pcap-file-packet-for-packet-using-python-scapy;
         More info on each with the "help()" command
        The "filter" parameter in "sniff" method is not working in Win10, even with npcap installed like recommended
        here: https://buildmedia.readthedocs.org/media/pdf/scapy/latest/scapy.pdf - p.20
        However, I personally think it might work with WinPcap, the predecessor of npcap.
        N.B.: During npcap installation, a "compatibility with WinPcap" checkbox appears which I think I didn't select.
        Might be the reason it doesn't properly work."""
        return sniff(offline=file_path, store=True)
        # "filter" parameter requires tcpdump (linux) or npcap/winpcap (windows)
        # "store" argument when set to False will delete current packet instance from memory, after function passed
        # in the "prn" function finishes processing

    def read_lines_csv_file(self, file_path, delim):
        with open(file_path, mode="rt", encoding="utf-8") as csv_file:
            for line in csv.reader(csv_file, delimiter=delim):
                yield line

    def read_lines_file(self, file_path):
        """ Generator method.
        """
        with open(file_path, mode="rt", encoding="utf-8") as file:
            while (line := file.readline()) != "":
                # The EOF char is an empty string
                yield line.rstrip("\n")

    def read_json_file(self, file_path):
        with open(file_path, mode="rt", encoding="utf-8") as json_file:
            for entry in json.load(json_file):
                yield entry
