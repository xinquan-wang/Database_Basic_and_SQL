import sys
import json

sys.stdout = open('csv_table_test', 'w')

sys.path.append('/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/src')
from CSVDataTable import CSVDataTable


def test_create_it():
    tbl = CSVDataTable("People",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "People.csv"
                       },
                       ['playerID'], None)
    tbl.load()
    print("First table = ", tbl)


def test_matches():
    tbl = CSVDataTable("People",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "People.csv"
                       },
                       ['playerID'], None)
    tbl.load()
    print("First table = ", tbl)
    tmp = {"nameLast": "Aardsma", "nameFirst": "Dave"}
    result = tbl.matches_template(tmp, tbl._rows[0])
    print("Match = ", result)


def test_tmp1():

    tbl = CSVDataTable("People",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "People.csv"
                       },
                       ['playerID'], None)
    tbl.load()
    print("First table = ", tbl)
    tmp = {"nameLast": "Williams", "throws": "R"}
    result = tbl.find_by_template(tmp, field_list=['playerID', 'nameLast', 'birthCity', 'throws'])
    print("\n\n After find by template, Result = ", result)

    tmp2 = {'birthCity': 'San Diego'}
    result2 = result.find_by_template(tmp2)
    print("\n\n After find by template find by template, Result = ", result2)


def test_key():

    tbl = CSVDataTable("People",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "People.csv"
                       },
                       ['playerID'], None)
    tbl.load()
    print("First table = ", tbl)

    result = tbl.find_by_primary_key(['willite01'], field_list=['playerID', 'nameLast'])
    print("\n\nResult = ", result)


def test_insert():

    tbl = CSVDataTable("offices",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "offices.csv"
                       },
                       ['officeCode'], None)
    tbl.load()
    print("First table = ", tbl)

    tmp = {"city": "Tokyo"}
    result1 = tbl.find_by_template(tmp)
    print("\n\nbefore insert =", result1)

    new_r = {
        'officeCode': '300',
        'city': 'Tokyo'
    }
    result = tbl.insert(new_r)


    result2 = tbl.find_by_template(tmp)
    print("\n\nafter insert =", result2)


def test_delete():

    tbl = CSVDataTable("offices",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "offices.csv"
                       },
                       ['officeCode'], None)
    tbl.load()
    print("First table = ", tbl)

    tmp = {"city": "Paris"}
    result1 = tbl.find_by_template(tmp)
    print("\n\nbefore delete =", result1)

    result = tbl.delete_by_template(tmp)
    print("\n\nI deleted ... ", result, "rows")


    result2 = tbl.find_by_template(tmp)
    print("\n\nafter delete =", result2)


def test_delete_by_key():

    tbl = CSVDataTable("offices",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "offices.csv"
                       },
                       ['officeCode'], None)
    tbl.load()
    print("First table = ", tbl)

    tmp = {"city": "Paris"}
    result1 = tbl.find_by_template(tmp)
    print("\n\nbefore delete =", result1)

    result = tbl.delete_by_key(key_fields=["4"])
    print("\n\nI deleted ... ", result, "rows")

    result2 = tbl.find_by_template(tmp)
    print("\n\nafter delete =", result2)


def test_update():
    tbl = CSVDataTable("offices",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "offices.csv"
                       },
                       ['officeCode'], None)
    tbl.load()

    tmp = {'city': "Paris"}
    new_v = {"officeCode": 13, "state": "Mars", "country": "Jupiter"}

    tbl.update_by_template(tmp, new_v)

    result = tbl.find_by_template(tmp)
    print("\n\nAfter update ... ", result)


def test_update_by_key():
    tbl = CSVDataTable("offices",
                       {
                           "directory": "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data",
                           "file_name": "offices.csv"
                       },
                       ['officeCode'], None)
    tbl.load()

    key_field = "4"
    new_v = {"officeCode": 13, "state": "Mars", "country": "Jupiter"}

    tbl.update_by_key(key_field, new_v)

    tmp = {'city': "Paris"}
    result = tbl.find_by_template(tmp)
    print("\n\nAfter update ... ", result)



test_create_it()
test_matches()
test_tmp1()
test_key()
test_insert()
test_delete()
test_delete_by_key()
test_update()
test_update_by_key()