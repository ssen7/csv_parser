from csv_parser import *

doContinue = True
while doContinue:

    try:
        file_name = str(input('Enter filepath: '))
        data, nrows, ncols, nfails, hline = csv_reader(file_name)
    except FileNotFoundError:
        print('Enter valid file name')
        continue

    print('Number of rows read successfully: {}'.format(nrows))
    print('Number of rows read unsuccessfully: {}'.format(nfails))

    doQuery = str(input('Do you want to query the data (Y/N): '))

    while doQuery.lower() == 'y':
        print('File Headers: ' + str(hline))
        keys = str(
            input('Enter the columns you want to search (comma separated): '))
        values = str(
            input('Enter the values you want to search (comma separated): '))

        keys = [x.strip() for x in keys.split(',')]

        values = [x.strip() for x in values.split(',')]

        indices = search_multiple(data, keys, values)

        jsondata = json.dumps(return_rows(data, indices), indent=4)

        if indices == None:
            # print('Header not present in data!')
            continue

        searchNumber = len(indices)
        doPrintRows = str(
            input('Do you want to print the {} rows (Y/N): '.format(searchNumber)))

        if doPrintRows.lower() == 'y':

            print(jsondata)

        doSaveRows = str(input('Do you want to save the rows to file (Y/N): '))

        if doSaveRows.lower() == 'y':

            save_file_name = str(input('Enter file name to be saved: '))

            with open(save_file_name + '.json', 'w') as outfile:
                json.dump(jsondata, outfile, indent=4)

        doContinueQueryYN = input('Do you want to continue query? (Y/N) ')

        if doContinueQueryYN.lower() == 'n':
            doQuery = 'n'

    doContinueYN = input('Do you want to read another file? (Y/N) ')

    if doContinueYN.lower() == 'n':
        doContinue = False
