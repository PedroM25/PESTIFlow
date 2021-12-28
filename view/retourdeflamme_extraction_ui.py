from controller.retourdeflamme_extraction_controller import RetourDeFlammeExtractionController
from view.extraction_ui import ExtractionUI


class RetourDeFlammeExtractionUI(ExtractionUI):

    def __init__(self, intro) -> None:
        super().__init__(intro)

    def display(self, input_path, output_path, gt_path):
        ctrl = RetourDeFlammeExtractionController()

        if gt_path is not None:
            print(f"Reading ground truth info present in \"{gt_path}\"...")
            ctrl.read_ground_truth(gt_path)
            print("Successfully read ground truth info.")

        print(f"Reading and analyzing entries present in \"{input_path}\"...")
        rao = ctrl.read_and_analyze_entries(input_path)
        print(f"- Total number of entries read: {rao.n_read_data_instances}")
        print(f"- Number of valid entries: {rao.n_valid_instances}")
        print(f"- Number of invalid entries: {rao.n_invalid_instances}")

        print("Performing feature extraction...")
        ctrl.obtain_feature_vectors()
        print("Feature extraction successful. " + f"Outputting extracted features to \"{output_path}\"...")
        bytes_written = ctrl.write_to_file(output_path)
        print(f"Operation completed successfully. {bytes_written} bytes were written.")
