from controller.cicids2018_extraction_controller import CICIDS2018ExtractionController
from view.extraction_ui import ExtractionUI


class CICIDS2018ExtractionUI(ExtractionUI):

    def display(self, input_path, output_path):
        ctrl = CICIDS2018ExtractionController()

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
