from controller.graylog_extraction_controller import GraylogExtractionController
from view.extraction_ui import ExtractionUI


class GraylogExtractionUI(ExtractionUI):

    def __init__(self, intro) -> None:
        super().__init__(intro)

    def display(self, input_path, output_path, gt_path):
        ctrl = GraylogExtractionController()

        if gt_path is not None:
            print(f"Reading ground truth info present in \"{gt_path}\"...")
            ctrl.read_ground_truth(gt_path)
            print("Successfully read ground truth info.")

        print(f"Reading and analyzing JSON entries present in \"{input_path}\"...")
        rao = ctrl.read_and_analyze_entries(input_path)
        print(f"- Total number of JSON entries read: {rao.n_read_data_instances}")
        print(f"- Number of valid JSON entries: {rao.n_valid_instances}")
        print(f"- Number of invalid JSON entries: {rao.n_invalid_instances}")

        print("Performing feature extraction...")
        ctrl.obtain_feature_vectors()
        print("Feature extraction successful. " + f"Outputting extracted features to \"{output_path}\"...")
        bytes_written = ctrl.write_to_file(output_path)
        print(f"Operation completed successfully. {bytes_written} bytes were written.")
