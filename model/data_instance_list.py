class DataInstanceList:
    """ do note that data instance can be anything, it can be a list of packets, a list containing several values
    obtained from a line of a CSV, etc. what is a data instance is defined by the what each algorithm needs to
    perform the extraction/calculation of features
    """

    def __init__(self):
        self._data_instances = []

    def add_data_instance(self, di):
        """ This append can be for anything that the developer wants. For example, in the case of pcap files,
        each Flow instance will hold several packets. When reading cicids2018 dataset, each Flow instance will only
        hold one list equivalent to one CSV line which is in turn, equivalent to one flow
        """
        self._data_instances.append(di)

    def __iter__(self):
        return iter(self._data_instances)
