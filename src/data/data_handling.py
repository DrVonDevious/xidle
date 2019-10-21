import json
import os, os.path
from pathlib import Path
from src import stats

def login():

    stats.name = input("Welcome to XIdle! What is your name?: ")

    if(Path('saves/' + stats.name.capitalize()).exists()):
        pass
    else:
        os.mkdir('saves/' + stats.name.capitalize())

def save():

    data = {}

    data['info'] = []
    data['score'] = []
    data['resources'] = []
    data['workers'] = []

    data['info'].append({
        'name': stats.name,
        'unlocks': stats.unlocks
    })

    data['score'].append({ 'score': stats.score })

    data['resources'].append({
        'gold': stats.gold,
        'wheat': stats.wheat,
        'lumber': stats.lumber 
    })

    data['workers'].append({ 
        'miners': stats.miners,
        'farmers': stats.farmers,
        'woodcutters': stats.woodcutters
    })

    with open('saves/' + stats.name.capitalize() + '/data.txt', 'w') as outfile:
        json.dump(data, outfile)
        print('Saving...')

def load():

    with open('saves/' + stats.name.capitalize() + '/data.txt') as json_file:
        data = json.load(json_file)
        print('Loading...')
        for i in data['info']:
            stats.name = i['name']
            stats.unlocks = i['unlocks']

        for s in data['score']:
            stats.score = s['score']
        
        for r in data['resources']:
            stats.gold = r['gold']
            stats.wheat = r['wheat']
            stats.lumber = r['lumber']

        for w in data['workers']:
            stats.miners = w['miners']
            stats.farmers = w['farmers']
            stats.woodcutters = w['woodcutters']