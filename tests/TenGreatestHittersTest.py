import sys
import json
import time
import csv
from operator import itemgetter

sys.stdout = open('TenGreatestHittersTest.txt', 'w')

sys.path.append('/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/src')
from CSVDataTable import CSVDataTable
from RDBDataTable import RDBDataTable
import TenGreatestHitters


## RDB
def test_query():
    t = RDBDataTable("Batting", ['playerID'])

    q = """SELECT 
            Batting.playerID, 
            (SELECT People.nameFirst FROM People WHERE People.playerID=Batting.playerID) as first_name, 
            (SELECT People.nameLast FROM People WHERE People.playerID=Batting.playerID) as last_name, 
            sum(Batting.h)/sum(batting.ab) as career_average, 
            sum(Batting.h) as career_hits, 
            sum(Batting.ab) as career_at_bats,
            min(Batting.yearID) as first_year, 
            max(Batting.yearID) as last_year 
            FROM 
            Batting 
            GROUP BY 
            playerId 
            HAVING 
            career_at_bats > 200 AND last_year >= 1960 
            ORDER BY 
            career_average DESC 
            LIMIT 10; """

    result = t._run_q(q)
    print("Result = ", json.dumps(result, indent=2))


test_query()


## CSV

data_dir = "/Users/wangxinquan/Desktop/2sem/W4111Database/HW1_xw2566/data/"

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

    for a in appearances:
        if a['yearID'] >= '1960':
            p = result.get(a['yearID'] , None)
            if p is None:
                result[a['playerID']] = "c"
    return list(result.keys())


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



start_time = time.time()
people = load("People.csv")
batting = load("Batting.csv")
appearances = load("Appearances.csv")
loaded_time = time.time()

eligible_players = compute_eligible_people()

final_result = total_people()
final_result = sorted(final_result, reverse=True, key=itemgetter(1))
final_result = final_result[0:10]

add_names()
end_time = time.time()

print("\n\nTen greatest hitters: ", json.dumps(final_result, indent=2))

print("\n\n")

print("Loading time = ", round(loaded_time - start_time, 3))
print("Elapsed time = ", round(end_time - start_time, 3))









