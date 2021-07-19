import json

team_images = json.load(open('team_images.json',encoding="utf8"))
team = json.load(open('team.json',encoding="utf8"))

for i in range(len(team)):
    team[i]['image'] = team_images[i]['image']

with open("team_merged.json", "w") as outfile:
    json.dump(team, outfile )