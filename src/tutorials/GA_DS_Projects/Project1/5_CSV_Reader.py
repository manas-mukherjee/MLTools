from collections import namedtuple
import re


def row_conversion(row, dtypes, header_values):
    for element_ind, row_element in enumerate(row):

        try:
            column_header = header_values[element_ind]
        except Exception as e:
            print(e)
            print("element_ind: {}".format(element_ind))

        if column_header in dtypes:
            column_type = dtypes[column_header]
            if column_type == int:
                try:
                    if row_element:
                        row[element_ind] = int(row_element)
                except Exception as e:
                    print("Exception: Type Conversion failed: e:".format(e))
                    if not row_element:
                        row_element = ""
                        print("ColumnType: {}, Column_header: {}, ColumnValue: {}".format(column_type, column_header,
                                                                                          row_element))

    return row


def read_csv(filename, dtypes={}, encoding='utf-8'):
    """ Returns a list of namedtuples.
    The fields in each namedtuple are specified by the header row."""
    rows = []

    # Your code here!
    try:
        datafile = open(filename, 'r')
        header_line = datafile.readline()
    except Exception as e:
        print("Exception: {}".format(e))

    if header_line:
        header_values = header_line[:-1].split(",")

        RowNamedTuple = namedtuple("Row", header_values)

        for row in datafile:
            if row:
                row_values = row[:-1].split(",")

            if len(dtypes) == 0:
                if len(row_values) > len(header_values):
                    continue
                    #I'll address this later. Comma withing a double-quoted element
                    # print("Parsing error. Skipping reocord")
                    # print("Error row: {}".format(row_values))
                else:
                    rowTuple = RowNamedTuple._make(row_values)
            else:
                row_values_with_type = row_conversion(row_values, dtypes, header_values)
                rowTuple = RowNamedTuple._make(row_values_with_type)
            rows.append(rowTuple)

    try:
        datafile.close()
    except Exception as e:
        print("Error while closing file: {}".format(e))

    return rows


rows = read_csv('./datasets/athletes-original.csv', dtypes={})
print(rows[:3])

# For the challenge problem only
dtypes = {'age': int, 'height': int, 'weight': int,
          'gold': int, 'silver': int, 'bronze': int, 'total': int}
rows = read_csv('./datasets/athletes-unquoted.csv', dtypes=dtypes)
print('')
print(rows[:3])