import json
import time

# start = time.time()


def csv_reader(filepath):
    '''
    Reads csv files.
    '''
    data_dict = {}

    with open(filepath) as file:
        hline = file.readline().strip().split(',')

        ncols = len(hline)
        nrows = 0
        nfails = 0

        data_dict = {k: [] for k in hline}
        for line in file:

            vals = line.strip().split(',')

            if len(vals) != len(hline):
                nfails += 1
                continue

            for i in range(len(hline)):

                data_dict[hline[i]] += [vals[i]]

            nrows += 1

    return data_dict, nrows, ncols, nfails, hline


def search(data, key, value):
    '''
    Searches one column of data.
    '''
    try:
        indices = [i for i, x in enumerate(data[key]) if x == value]
        return indices
    except KeyError:
        print('Header not present in data')


def search_multiple(data, keyL, valueL):
    '''
    Searches through multiple columns of data.
    '''
    try:
        indexList = []
        for key, value in zip(keyL, valueL):
            indices = [i for i, x in enumerate(data[key]) if x == value]
            indexList.append(indices)
        result = set(indexList[0]).intersection(*indexList[1:])
        # print(result)
        return result
    except KeyError:
        print('Header not present in data')


def return_rows(data, indices):
    '''
    Return rows from data based on indices.
    '''
    rowL = []
    if indices == None:
        return None
    for ind in indices:
        row = {}
        for key in data.keys():
            row[key] = data[key][ind]

        rowL.append(row)

    return rowL


def queryData(data, keys, values):

    indices = search_multiple(data, keys, values)
    return return_rows(data, indices)


def subsetData(data, indices):
    newdata = {k: [] for k in data.keys()}
    for key in data.keys():
        for i in indices:
            print(data[key][i])
            newdata[key] += [data[key][i]]

    return newdata


# data, _, _, _, _ = csv_reader('titanic.csv')

# newdata = subsetData(data, [1, 2])

# print(newdata)

# print('Time taken : {} s'.format(time.time() - start))

# indices = search_multiple(data, ['Longitude'], ['99999'])

# return_rows(data, indices)

# print(json.dumps(return_rows(data, indices), indent=4))

# jsondata = json.dumps(return_rows(data, indices), indent=4)
# with open('data.json', 'w') as outfile:
#     json.dump(jsondata, outfile, indent=4)

# print('Time taken : {} s'.format(time.time() - start))

# Additional Stuff
# multiple queries #done
# what if there are more rows like > 500, is it efficient
# check if header names are repeated
#
