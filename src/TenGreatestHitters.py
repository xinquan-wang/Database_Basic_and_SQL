import pymysql
import json
import csv
import time


from CSVDataTable import CSVDataTable


data_dir = "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data/"


## RDB
_default_connect_info = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Chloe1221',
        'db': 'HW1',
        'port': 3306
    }


_cnx = pymysql.connect(
            host=_default_connect_info['host'],
            user=_default_connect_info['user'],
            password=_default_connect_info['password'],
            db=_default_connect_info['db'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


def _run_q(q, args=None, fields=None, fetch=True, cnx=None, commit=True):
    """

    :param q: An SQL query string that may have %s slots for argument insertion. The string
        may also have {} after select for columns to choose.
    :param args: A tuple of values to insert in the %s slots.
    :param fetch: If true, return the result.
    :param cnx: A database connection. May be None
    :param commit: Do not worry about this for now. This is more wizard stuff.
    :return: A result set or None.
    """

    # Use the connection in the object if no connection provided.
    if cnx is None:
        cnx = _cnx

    # Convert the list of columns into the form "col1, col2, ..." for following SELECT.
    if fields:
        q = q.format(",".join(fields))

    cursor = cnx.cursor()  # Just ignore this for now.

    # If debugging is turned on, will print the query sent to the database.
    print("Query = ", cursor.mogrify(q, args))

    cnt = cursor.execute(q, args)  # Execute the query.

    # Technically, INSERT, UPDATE and DELETE do not return results.
    # Sometimes the connector libraries return the number of created/deleted rows.
    if fetch:
        r = cursor.fetchall()  # Return all elements of the result.
    else:
        r = cnt

    if commit:  # Do not worry about this for now.
        cnx.commit()

    return r


## CSV

def load(fn):
    result = []
    fn = data_dir + fn
    with open(fn, "r") as csvfile:
        c_reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        for r in c_reader:
            result.append(r)
    return result


def compute_eligible_people():
    result = {}
    appearances = load("Appearances.csv")
    for a in appearances:
        if a['yearID'] >= '1960':
            p = result.get(a['yearID'] , None)
            if p is None:
                result[a['playerID']] = "c"
    eligible_players = list(result.keys())
    return eligible_players


def career_stats(p):
    total_hits = 0
    total_abs = 0

    for b in batting:
        if b['playerID'] == p:
            total_hits += int(b['H'])
            total_abs += int(b['AB'])

    avg = 0
    if total_abs > 0:
        avg = total_hits / total_abs

    return [p, avg, total_hits, total_abs]



def total_people():
    result = []
    count = 0

    for p in eligible_players:
        bat = career_stats(p)
        count += 1

        if count % 100 == 0:
            print("Did eligible ", count, " current = ", bat)
        if bat[3] > 200:
            result.append(bat)

    return result


def add_names():
    for f in final_result:

        pid = f[0]
        for p in people:
            if p['playerID'] == pid:
                f.append(p['nameLast'])
                f.append(p['nameFirst'])


