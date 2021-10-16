import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']

def search_most_intelligent(names_list):
    dict = {}
    for name in names_list:
        response = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{name}')
        intelligence = response.json()['results'][0]['powerstats']['intelligence']
        dict.update({name: int(intelligence)})
    high_intelligence = 0
    name_hero = ''
    for name, stat in dict.items():
        if stat > high_intelligence:
            high_intelligence = stat
            name_hero = name
    print(f'Самый умный супергерой: {name_hero} ({high_intelligence} баллов)')



search_most_intelligent(hero_list)
