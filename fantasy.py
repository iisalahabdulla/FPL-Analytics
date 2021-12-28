import requests
import json
from tabulate import tabulate 

headers= ["Rank", "Name", "Team Name", "Total points spent","Last Minus", "Current GW", "All GWs"]

session = requests.session()
url = 'https://users.premierleague.com/accounts/login/'
payload = {
 'password': 'password',
 'login': 'username',
 'redirect_uri': 'https://fantasy.premierleague.com/a/login',
 'app': 'plfpl-web'
}
session.post(url, data=payload)
leagueid = input("Enter League id: ")
currgw = input("Enter gameweek: ")
currgw += 1
response = session.get('https://fantasy.premierleague.com/api/leagues-classic/{0}/standings/'.format(leagueid))
print("\n")
parsed = json.loads(response.content)
results = parsed['standings']['results']
mydata = []
counter = 0
print(parsed)
for team in results:
    teamid = str(team['entry'])
    print (teamid)
    if teamid != "8007849":
        pointSpent = 0
        print(counter)
        for i in range(2, currgw):
            ii = str(i)
            response2 = session.get('https://fantasy.premierleague.com/api/entry/{0}/event/{1}/picks/'.format(teamid, ii))
            parsed2 = json.loads(response2.content)
            pointsgwspent = parsed2['entry_history']['event_transfers_cost']
            print(f"ID: {teamid}   GameWeek: {ii}  => {pointsgwspent}")
            pointSpent += pointsgwspent
        print("___________________________________________________")
        lastPointCost = pointsgwspent
        mydata.append([str(team['rank']), team['player_name'],team['entry_name'], str(pointSpent),str(lastPointCost), str(team['event_total']), str(team['total'])])

        counter = counter + 1
    #print("Total points spent is: " + str(pointSpent))
    #print(team)
    
print(tabulate(mydata, headers=headers, tablefmt="grid"))






