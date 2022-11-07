# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


class DummyData:
    def __init__(self, indicator, datafilter):
        self.standard_filters: list = [Filter("time_period"), Filter("geographic_level")]
        if isinstance(indicator, Indicator):
            self.indicators = [indicator]
        elif isinstance(indicator, list):
            self.indicators = indicator
        if isinstance(datafilter, Filter):
            self.custom_filters = [datafilter]
        elif isinstance(datafilter, list):
            self.custom_filters = datafilter

    def add_indicator(self, indicator):
        self.indicators.append(indicator)

    def add_filter(self, datafilter):
        # Should add some validation code to check
        #   a) it's a filter
        #   b) give a warning if the stated filter_grouping_column doesn't exist
        self.custom_filters.append(datafilter)

    def create_data(self):
        # This should create some sort of data frame type object that represents the
        # contents of the data file, based on the defined indicators and filters
        pass

    def create_meta(self):
        # This should create some sort of data frame type object that represents the
        # contents of the meta-data file, based on the defined indicators and filters
        pass

    def write_files(self, stem):
        pass


class Filter:
    def __init__(self, col_name, label, filter_hint='', filter_grouping_column=''):
        # Possible additional attributes I'd be wanting in here:
        #   a) adding some definitions over which other filters it's broken down with
        #   b) list of filter values to include
        #   c) could create some specific sub-classes for geography, time period etc.
        self.col_name = col_name
        self.label = label
        self.filter_hint = filter_hint
        self.filter_grouping_column = filter_grouping_column

        def initialise_filter(self):
            filter = np.arange(0, range)
            print(filter)


class Indicator:
    def __init__(self, col_name, label, data_type, data_range, indicator_grouping='', indicator_unit='', indicator_dp=''):
        self.col_name = col_name
        self.label = label
        self.indicator_grouping = indicator_grouping
        self.indicator_unit = indicator_unit
        self.indicator_dp = indicator_dp

    def initialise_indicator(self):
        if self.data_type=='numeric':
            self.indicator_data = np.arange(0,self.data_range)
            print(self.indicator_data)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    initialise_indicator("name",10)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
