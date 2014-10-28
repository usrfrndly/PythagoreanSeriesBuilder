"""
HarmonicSeriesRow.py
Jaclyn Horowitz
Music Software Projects 2014
"""

import math

'''
PythagSeriesColumn class : Represents an interval column in the pythagorean series and is initialized with a
 interval degree and a base frequency.
'''


class PythagSeriesColumn(object):

    def __init__(self, interval, basefrq):
        self.base_frequency = basefrq
        self.interval = int(interval)
        self.numerator = self.get_numerator()
        self.denom = self.get_denom()
        self.factor = self.get_factor()
        self.frequency = self.get_frequency()
        self.octave = self.get_octave()
        self.octave_denom = self.get_octave_denom()
        self.factor_reduced = self.get_factor_reduced()
        self.final_frequency = self.get_final_frequency()

    def __repr__(self):
        return '{}: {}, {}, {}, {}, {}, {}, {}, {}, {} '.format(self.__class__.__name__,self.interval, self.numerator,
            self.denom, self.factor, self.frequency, self.octave, self.octave_denom, self.factor_reduced,self.final_frequency)


    '''
    Methods that calculate properties for a row in the HarmonicSeries
    '''

    def get_numerator(self):
        if self.interval == -1:
            return 2
        else:
            return math.pow(3, self.interval)

    def get_frequencytofundamental(self):
        return "\"" + str(self.interval) + "/1\""

    def get_octave(self):
        return math.floor(self.interval/2)

    def get_factor(self):
        return self.numerator/self.denom

    def get_octave_denom(self):
        return math.pow(2, self.octave)

    def get_denom(self):
        if self.interval == -1:
            return 3
        else:
            return math.pow(2, self.interval)

    def get_frequency(self):
        return self.base_frequency * self.factor

    def get_factor_reduced(self):
        return self.factor/self.octave_denom

    def get_final_frequency(self):
        return round(self.base_frequency * self.factor_reduced,2)

    # to_array(): Returns an array representation of the properties of a row in the HarmonicSeries, which
    # orders the properties the same as in the csv file
    def to_array(self):
        return [self.interval, self.numerator, self.denom, self.factor, self.frequency, self.octave,
                self.octave_denom, self.factor_reduced, self.final_frequency]

    # show_row(): Returns a string representation of the properties of a row in the HarmonicSeries
    def show_column(self):
        # [interval, frequencytofundamental, frequency, octave, denom, ratio, ratio_reduced, decimal,freqinlowestoctave]
        print("[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8} ".format(str(self.interval), self.numerator,
            str(self.denom), str(self.factor), str(self.frequency), self.octave, self.octave_denom, str(self.factor_reduced),self.final_frequency))
