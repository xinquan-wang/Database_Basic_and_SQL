import sys
import json

sys.stdout = open('rdb_table_test.txt', 'w')

sys.path.append('/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/src')
from RDBDataTable import RDBDataTable


def test1():
    t = RDBDataTable("People", ['playerID'])
    print(t)


def test2():
    t = RDBDataTable("People", ['playerID'])

    tmp = { "nameLast": "Williams", "nameFirst": "Ted"}
    result = t._template_to_where_clause(tmp)
    print("WC = ", str(result))

    q = "select * from People " + result[0]
    print("Query = ", q)

    result = t._run_q(cnx=None, q=q, args=result[1], commit=True, fetch=True)
    print("Query result = ", json.dumps(result, indent=2))


def test3():
    t = RDBDataTable("People", ['playerID'])

    tmp = { "nameLast": "Williams", "nameFirst": "Ted"}

    result = t.find_by_template(tmp, field_list=['playerID', 'nameLast', 'throws'])
    print("Result = ", result)


def test4():
    t = RDBDataTable("People", ['playerID'])

    tmp = { "nameLast": "Williams", "nameFirst": "Ted"}

    result = t.find_by_template(tmp, field_list=['playerID', 'nameLast'])

    print("Result = ", result)


def test5():
    t = RDBDataTable("People", key_columns=['playerID'], debug=True)

    result = t.find_by_primary_key(["willite01"], field_list=['playerID', 'nameLast', 'throws'])

    print("\n\nResult = ", result)


def test6():
    t = RDBDataTable("People", key_columns=None, debug=True)

    result = t._get_primary_key()

    print("\n\nResult = ", json.dumps(result, indent=2))


def test7():
    t = RDBDataTable("People", key_columns=None, debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("\n\nResult = ", json.dumps(result, indent=2))

    tmp = {'playerID': 'dff201'}
    r1 = t.find_by_template(tmp)
    print("\n\nAfter insert, Q returns ", r1)


def test8():
    t = RDBDataTable("People", key_columns=None, debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("Result = ", json.dumps(result, indent=2))

    tmp = {'playerID': 'dff201'}
    r1 = t.find_by_template(tmp)
    print("\n\nAfter insert, Q returns ", r1)

    result = t.delete_by_template({'playerID': 'dff201'})
    print("\n\nAfter delete, Q returns ", result)


def test9():
    t = RDBDataTable("People", key_columns=['playerID'], debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("\n\nResult = ", json.dumps(result, indent=2))

    tmp = {'\n\nplayerID': 'dff201'}
    r1 = t.find_by_template(tmp)
    print("After insert, Q returns ", r1)

    result = t.delete_by_key(key_fields=['dff201'])
    print("\n\nAfter delete, Q returns ", result)


def test10():
    t = RDBDataTable("People", key_columns=['playerID'], debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("Result = ", json.dumps(result, indent=2))

    tmp = {'playerID': 'dff201'}

    new_c = {
        "nameFirst": "Donald",
        "bats": "R"
    }

    r1 = t.update_by_template(tmp, new_c)
    print("\n\nAfter update, Q returns ", r1)

    result = t.delete_by_template({'playerID': 'dff201'})
    print("\n\nAfter delete, Q returns ", result)


def test11():
    t = RDBDataTable("People", key_columns=['playerID'], debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("Result = ", json.dumps(result, indent=2))

    new_c = {
        "nameFirst": "Donald",
        "bats": "R"
    }

    r1 = t.update_by_key(key_fields=['dff201'], new_values=new_c)
    print("\n\nAfter update, Q returns ", r1)

    result = t.delete_by_template({'playerID': 'dff201'})
    print("\n\nAfter delete, Q returns ", result)


test1()
test2()
test3()
test4()
test5()
test6()
test7()
#test8()
#test9()
#test10()
#test11()