from abc import ABC

from model.ground_truth import GroundTruth
from model.services.io_service import IOService


class ExtractionController(ABC):
    """ This class must NOT be instantiated.
    """

    def __init__(self) -> None:
        self.ground_truth = None
        self.calculated_fv = None
        self.ext_alg = None

    def read_ground_truth(self, gt_path):
        """ This method could very well not return anything but its useful, in this case that it does
        """
        self.ground_truth = GroundTruth(gt_path)

    def write_to_file(self, output_path):
        return IOService().write_feature_vectors_to_csv(output_path, self.calculated_fv)

    def obtain_feature_vectors(self):
        """ This method could very well not return anything but its useful, in this case that it does
        """
        self.calculated_fv = self.ext_alg.execute()
