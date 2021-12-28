import utilities
from model.data_instance_list import DataInstanceList
from model.factories.feature_vector_factory import FeatureVectorFactory
from model.feature_vector_list import FeatureVectorList
from model.uni_features_interface import UniFeaturesInterface


class UniExtractionAlgorithm(UniFeaturesInterface):
    """ This class must NOT be instantiated. Everything is received in the constructor instead of each method because
    the only reasons there are multiple methods is to make the UI more dynamic and display info as the program
    progresses
    """

    def __init__(self, ground_truth):
        """ ground_truth is an instance attribute because of architecture devised for feature extraction.
        data_instances_per_flow is Result from analyzing the read data instances (can have one or more data
        instances); doesn't make sense to store it in the controller since it's temporary
        """
        self.ground_truth = ground_truth
        self.data_instances_per_flow = DataInstanceList()

    def execute(self):
        all_fv = FeatureVectorList()
        factory = FeatureVectorFactory()
        for current_data_instances in self.data_instances_per_flow:
            fv = factory.create_feature_vector(self)

            for feature in fv.all_features():
                try:
                    calc_current_feature = getattr(self, feature)
                    if (value := calc_current_feature(current_data_instances)) is not None:
                        setattr(fv, feature, value)
                except AttributeError:
                    pass
            all_fv.add_feature_vector(fv)
        return all_fv

    def label(self, dict_entry):
        if self.ground_truth is not None:
            return self.ground_truth.flow_status(self.src_ip(dict_entry),
                                                 self.dst_ip(dict_entry),
                                                 self.ts_beginning(dict_entry),
                                                 self.ts_end(dict_entry))
        else:
            return
            # when no ground truth file is specified

    def attack_type(self, dict_entry):
        if self.ground_truth is not None:
            attack_type = self.ground_truth.get_attack_type(self.src_ip(dict_entry),
                                                            self.dst_ip(dict_entry),
                                                            self.ts_beginning(dict_entry),
                                                            self.ts_end(dict_entry))
            if attack_type is not None:
                return attack_type
            else:
                return utilities.NOT_AVAILABLE
                # no attack type string was specified in the line/attack matching with the passed info, in the gt file
                # OR no attack with the provided info was given in the ground truth file so, no attack_type exists
                # This is also what appears in feature vectors related to responses from a victim to an attacker
        else:
            return
            # when no ground truth file is specified

    def fw_pkt_l_avg(self, packets_of_flow):
        try:
            return self.tot_l_fw_pkt(packets_of_flow) / self.tot_fw_pkt(packets_of_flow)
        except ZeroDivisionError:
            return utilities.NOT_AVAILABLE

    def land(self, dict_entry):
        if self.src_ip(dict_entry) == self.dst_ip(dict_entry) \
                and self.src_port(dict_entry) == self.dst_port(dict_entry):
            return int(True)
        return int(False)

    def fl_dur(self, dict_entry):
        delta = self.ts_end(dict_entry) - self.ts_beginning(dict_entry)
        return delta.total_seconds()
