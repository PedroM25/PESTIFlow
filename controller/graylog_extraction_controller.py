from controller.extraction_controller import ExtractionController
from model.algorithms.airbus.graylog_extraction_algorithm import GraylogExtractionAlgorithm


class GraylogExtractionController(ExtractionController):

    def read_and_analyze_entries(self, input_path):
        """ This method could very well not return anything but its useful, in this case that it does"""
        self.ext_alg = GraylogExtractionAlgorithm(self.ground_truth)
        return self.ext_alg.read_and_analyze_json_entries(input_path)
