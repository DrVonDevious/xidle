import json
from src import stats

def save():

    data = {}

    data['score'] = []
    data['resources'] = []
    data['workers'] = []

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

    with open('saves/data.txt', 'w') as outfile:
        json.dump(data, outfile)
        print('Saving...')

def load():

    with open('saves/data.txt') as json_file:
        data = json.load(json_file)
        print('Loading...')
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