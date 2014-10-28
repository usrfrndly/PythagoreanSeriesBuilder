'''
PythagSeriesTest.py : A test suite that compares values actual values derived from the PythagSeries class
to a CSV file containing the expected values
The base frequency noted in the main method of PythagSeries.py should equal the basefrequency in the csv file

Jaclyn Horowitz
Music Software 2014
'''
import csv
import math

csv_list = []
# Change csv file to be compared to here
with open('pythag_sheet_phase2.csv', 'rU') as my_file:
    reader = csv.reader(my_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
    # Skip all empty rows
    for row in reader:
        newrow = []
        for cell in row:
            if cell != '':
                newrow.append(cell)
        if len(newrow) != 0:
            csv_list.append(row)
    # find the first data column
    title_row = 0
    for r in csv_list:
        if r[0] == 'Interval number':
            break
        else:
            title_row += 1
    csv_list = csv_list[title_row:]

my_file.close()

# test_all_cells(harmonic_series): accepts a PythagSeries object as a parameter and compares
# every property in each calculated interval column to the corresponding column and cell in a csv file
def test_all_cells(pythag_series):
    print("*** Beginning test_all_cells() tests ***")
    # How many tests failed
    failed = 0
    # The index in the interval list array (which column)
    interval_index = 0
    for interval in pythag_series.interval_list:
            # The index of the property (which row)
            prop_index = 0
            # Return the column in the pythag series array for a specific interval
            pythag_interval_array = pythag_series.series_columns[interval_index].to_array()
            print("interval: " + str(interval) + "intervalIndex:" + str(interval_index))
            print("pythag array: " + str(pythag_interval_array))

            # Iterate through each property of the interval
            for prop in pythag_interval_array:
                # The 0 interval does not have data for many properties in the csv
                if interval == 0 and prop_index != 0 and prop_index != 7:
                    continue
                else:
                    # The first column for each property row is the name of the property
                    prop_name = csv_list[prop_index][0]
                    # Return a property at a certain interval index
                    csv_prop = float(csv_list[prop_index][interval_index+1])
                    print("prop_name: " + prop_name + "propIndex: " + str(prop_index) + "function prop: " + str(prop) + "csv_prop: " + str(csv_prop))
                    # Check if the csv property and the calculated property match
                    if not eq(csv_prop, prop):
                        print("INCORRECT: For Interval %s and Property %s CSV Cell = %s , Calculated  = %s" % (
                            interval, str(prop_name), csv_prop, prop))
                        failed += 1
                    else:
                        print("CORRECT: Interval " + str(interval) + ": Property " + prop_name + ". For Value: " + str(prop))
                prop_index += 1
            interval_index += 1

    print("*** test_all_cells() SUMMARY *** ")
    print("Failed: %d " % failed)



def eq(a, b, eps=0.001):
     return abs(a - b) <= eps
