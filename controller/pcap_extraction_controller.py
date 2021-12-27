from controller.extraction_controller import ExtractionController
from model.factories.pcap_extraction_algorithm_factory import PcapExtractionAlgorithmFactory


class PcapExtractionController(ExtractionController):
    """ Normally, the cleanup_packets, obtain_flows would correspond to only one method inside the Algorithm but
    since I want to have different outputs in the UI, algorithm functionality was also split up to accommodate for
    that This implies that methods should be executed in the order they are presented in this file or the program
    could fail. (for example, if cleanup is not executed first, the program will fail)
    """

    def read_and_analyze_packets(self, input_path, timeout, bi_flows):
        """ may only be called once ground truth has been read
        """
        self.ext_alg = PcapExtractionAlgorithmFactory().create_pcap_extraction_algorithm(bi_flows, self.ground_truth)
        return self.ext_alg.read_and_analyze_data_instances(input_path, timeout)
