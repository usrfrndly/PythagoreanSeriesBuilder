"""
PythagSeries.py
Jaclyn Horowitz
Music Software Projects 2014
"""

import csv
import math
import struct
from PythagSeriesColumn import PythagSeriesColumn
import PythagSeriesTest
import pyaudio

'''
PythagSeries class : Represents the pythagorean series and is initialized with a base frequency.
'''


class PythagSeries(object):
    def __init__(self, base_fq):
        self.base_freq = base_fq
        # We are looking at the seven tone scale
        numintervals = 7
        self.interval_list = [-1, 0, 1, 2, 3, 4, 5]
        # An array that contains properties for each interval in the pythag series
        self.series_columns = [None] * numintervals
        self.generate_columns()

    # generate_columns(): adds information for each interval in the pythagorean series to the series_columns array
    def generate_columns(self):
        i = 0
        for interval in self.interval_list:
            self.series_columns[i] = self.generate_column(interval)
            i += 1

    # generate_column(): returns the PythagSeriesColumn object that contains properties about a
    # specific interval in the pythag series
    def generate_column(self, interval):
        col = PythagSeriesColumn(interval, self.base_freq)
        return col

    # get_frequency(interval) : Accepts an interval as a parameter and returns the corresponding interval frequency,
    # using the frequency property of the PythagSeriesRow class
    def get_frequency(self, interval):
        if interval in range(-1, 6):
            return self.series_columns[interval+1].frequency

    # get_interval_ratio(interval) : Accepts a pythag interval as a parameter and returns the ratio of
    # the interval to its lowest octave, using the ratio property of the PythagSeriesColumn class
    def get_interval_ratio(self, interval):
        if interval in range(-1, 6):
            return "\"" + str(int(self.series_columns[interval+1].numerator)) + "/" + str(int(self.series_columns[interval+1].denom)) + "\""

    # show_all_rows(): Prints each row in the pythagorithmic series
    def show_series_columns(self):
        print("[Interval, Numerator, Denominator, Factor,"
              " Interval Frequency, Octave, Octave Denom, Factor (Octave Adjusted), Final Frequency ]")
        for i in range(0, len(self.series_columns)):
            self.series_columns[i].show_column()

    # show(): prints all the cells in csv file that has a base frequency of 528 hertz
    def show_csv_rows(self):
        csv_list=[]
        with open('pythag_sheet_phase2.csv', 'rU') as my_file:
            reader = csv.reader(my_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
            # Skip all empty rows
            for row in reader:
                newrow = []
                for cell in row:
                    if cell != '':
                        newrow.append(cell)
                if len(newrow) != 0:
                    csv_list.append(newrow)
            # find the first data column
            title_row = 0
            for r in csv_list:
                if r[0] == 'Interval number':
                    break
                else:
                    title_row += 1
            csv_list = csv_list[title_row:]
            print(csv_list)
            my_file.close()

    # Sorts the pythag series from lowest to highest final frequency value
    def sortByFinalFrequency(self):
         return sorted(self.series_columns, key=lambda  x:x.final_frequency)

    # Plays the sorted pythag scale
    def play_scale(self):
        orderedList = self.sortByFinalFrequency()
        fs = 48000
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=fs,
            output=True)
        for interval in orderedList:
            print(interval)
            self.play_tone(interval.final_frequency,0.5,1,fs,stream)
        octave_note = self.base_freq*2
        # play octave note
        print(octave_note)
        self.play_tone(octave_note, 0.5, 1, fs, stream)
        stream.close()
        p.terminate()


    def play_tone(self,frequency, amplitude, duration, fs, stream):
        N = int(fs / frequency)
        T = int(frequency * duration)  # repeat for T cycles
        dt = 1.0 / fs
        # 1 cycle
        tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
                for n in range(N))
        #  =todo: get the format from the stream; this assumes Float32
        data = b''.join(struct.pack('f', samp) for samp in tone)
        for n in range(T):
            stream.write(data)




# main() : Creates a PythagSeries object given a base frequency, prints out each calculated row in the pythagorean series,
# and compares this calculated data with the csv data using functions in PythagSeriesTes
#You can also run the other methods get_frequency(interval) and get_ratio(interval) on the pythag_series object
def main():
    # Change base_frequency manually
    base_frequency = 528
    print("Your base frequency is %d hertz" % base_frequency)
    pythag_series = PythagSeries(base_frequency)
    #pythag_series.show_series_columns()
    #pythag_series.show_csv_rows()
    pythag_series.play_scale()
    PythagSeriesTest.test_all_cells(pythag_series)
    #print(pythag_series.get_frequency(-1))
    #print(pythag_series.get_interval_ratio(4))

if __name__ == '__main__':
    main()


