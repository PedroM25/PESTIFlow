from controller.pcap_extraction_controller import PcapExtractionController
from view.extraction_ui import ExtractionUI


class PcapExtractionUI(ExtractionUI):

    def __init__(self, intro, bi_flows):
        self.bi_flows = bi_flows
        super().__init__(intro)

    def display(self, input_path, output_path, gt_path, timeout):
        ctrl = PcapExtractionController()

        if gt_path is not None:
            print(f"Reading ground truth info present in \"{gt_path}\"...")
            ctrl.read_ground_truth(gt_path)
            print("Successfully read ground truth info.")

        print(f"Reading and analyzing packets present in \"{input_path}\"...")
        rao = ctrl.read_and_analyze_packets(input_path, timeout, self.bi_flows)
        print(f"- Total number of packets read: {rao.n_read_data_instances}")
        print(f"- Number of valid packets: {rao.n_valid_instances}")
        print(f"- Number of invalid packets: {rao.n_invalid_instances}")

        print("Performing feature extraction...")
        ctrl.obtain_feature_vectors()
        print("Feature extraction successful. " + f"Outputting extracted features to \"{output_path}\"...")
        bytes_written = ctrl.write_to_file(output_path)
        print(f"Operation completed successfully. {bytes_written} bytes were written.")

    def _print_intro(self, string):
        string += " - "
        if self.bi_flows:
            string += "bidirectional"
        else:
            string += "unidirectional"
        super()._print_intro(string)
