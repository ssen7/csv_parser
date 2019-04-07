import json
import time

start = time.time()


def csv_reader(filepath):

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

    try:
        indices = [i for i, x in enumerate(data[key]) if x == value]
        return indices
    except KeyError:
        print('Header not present in data')


def search_multiple(data, keyL, valueL):
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

    rowL = []
    if indices == None:
        return None
    for ind in indices:
        row = {}
        for key in data.keys():
            row[key] = data[key][ind]

        rowL.append(row)

    return rowL


# data, _, _ = csv_reader('los-angeles-parking-citations/parking-citations.csv')

# print('Time taken : {} s'.format(time.time() - start))

# indices = search_multiple(data, ['Longitude'], ['99999'])

# return_rows(data, indices)

# print(json.dumps(return_rows(data, indices), indent=4))

# jsondata = json.dumps(return_rows(data, indices), indent=4)
# with open('data.json', 'w') as outfile:
#     json.dump(jsondata, outfile, indent=4)

# print('Time taken : {} s'.format(time.time() - start))

# multiple queries #done
# what if there are more rows like > 500,
# what if header names are repeated
