# csv_parser

Run main.py to run the program

test run:

```
Enter filepath: titanic.csv
Number of rows read successfully: 887
Number of rows read unsuccessfully: 0
Do you want to query the data (Y/N): y
File Headers: ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']
Enter the columns you want to search (comma separated): Age, Pclass, Sex
Enter the values you want to search (comma separated): 30, 2, male
Do you want to print the 5 rows (Y/N): y
[
    {
        "Survived": "0",
        "Pclass": "2",
        "Name": "Mr. William John Matthews",
        "Sex": "male",
        "Age": "30",
        "Siblings/Spouses Aboard": "0",
        "Parents/Children Aboard": "0",
        "Fare": "13"
    },
    {
        "Survived": "0",
        "Pclass": "2",
        "Name": "Mr. Reginald Hale",
        "Sex": "male",
        "Age": "30",
        "Siblings/Spouses Aboard": "0",
        "Parents/Children Aboard": "0",
        "Fare": "13"
    },
    {
        "Survived": "0",
        "Pclass": "2",
        "Name": "Mr. Samuel Abelson",
        "Sex": "male",
        "Age": "30",
        "Siblings/Spouses Aboard": "1",
        "Parents/Children Aboard": "0",
        "Fare": "24"
    },
    {
        "Survived": "0",
        "Pclass": "2",
        "Name": "Mr. Hans Kristensen Givard",
        "Sex": "male",
        "Age": "30",
        "Siblings/Spouses Aboard": "0",
        "Parents/Children Aboard": "0",
        "Fare": "13"
    },
    {
        "Survived": "0",
        "Pclass": "2",
        "Name": "Mr. Walter Harris",
        "Sex": "male",
        "Age": "30",
        "Siblings/Spouses Aboard": "0",
        "Parents/Children Aboard": "0",
        "Fare": "10.5"
    }
]
Do you want to save the rows to file (Y/N): y
Enter file name to be saved: test
Do you want to start new query? (Y/N) n
Do you want to read another file? (Y/N) n
```