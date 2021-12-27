from controller.extraction_controller import ExtractionController
from model.algorithms.airbus.retourdeflamme_extraction_algorithm import RetourDeFlammeExtractionAlgorithm


class RetourDeFlammeExtractionController(ExtractionController):

    def read_and_analyze_entries(self, input_path):
        """ This method could very well not return anything but its useful, in this case that it does
        """
        self.ext_alg = RetourDeFlammeExtractionAlgorithm(self.ground_truth)
        return self.ext_alg.read_and_analyze_entries(input_path)
