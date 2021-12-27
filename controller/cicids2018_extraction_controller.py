from controller.extraction_controller import ExtractionController
from model.algorithms.cicids2018_extraction_algorithm import CICIDS2018ExtractionAlgorithm


class CICIDS2018ExtractionController(ExtractionController):

    def read_and_analyze_entries(self, input_path):
        """ This method could very well not return anything but its useful, in this case that it does
        """
        self.ext_alg = CICIDS2018ExtractionAlgorithm(self.ground_truth)
        return self.ext_alg.read_and_analyze_entries(input_path)
