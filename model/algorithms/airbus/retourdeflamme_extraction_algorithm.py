import json
from json import JSONDecodeError

from model.algorithms.airbus.airbus_extraction_algorithm import AirbusExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput
from model.services.io_service import IOService


class RetourDeFlammeExtractionAlgorithm(AirbusExtractionAlgorithm):

    def read_and_analyze_entries(self, input_path):
        ra_output = ReadAnalyzeOutput()
        for current_entry in IOService().read_lines_file(input_path):
            ra_output.n_read_data_instances += 1
            split_entry = current_entry.split()
            try:
                dict_entry = json.loads(split_entry[-1])
                if not self.entry_is_valid(dict_entry):
                    ra_output.n_invalid_instances += 1
                    continue

            except (JSONDecodeError, KeyError):
                ra_output.n_invalid_instances += 1
                continue
            ra_output.n_valid_instances += 1

            self.data_instances_per_flow.add_data_instance(dict_entry)
        return ra_output
