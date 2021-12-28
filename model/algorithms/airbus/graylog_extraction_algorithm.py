import json
from json import JSONDecodeError

from model.algorithms.airbus.airbus_extraction_algorithm import AirbusExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput
from model.services.io_service import IOService


class GraylogExtractionAlgorithm(AirbusExtractionAlgorithm):

    def read_and_analyze_json_entries(self, input_path):
        ra_output = ReadAnalyzeOutput()
        for current_json_entry in IOService().read_json_file(input_path):
            ra_output.n_read_data_instances += 1
            try:
                sub_json_entry = json.loads(current_json_entry[self._SOURCE][self._MESSAGE.upper()])
                if not self.entry_is_valid(sub_json_entry):
                    ra_output.n_invalid_instances += 1
                    continue
                ra_output.n_valid_instances += 1
                self.data_instances_per_flow.add_data_instance(sub_json_entry)
            except (JSONDecodeError, KeyError):
                ra_output.n_invalid_instances += 1
                continue
        return ra_output
