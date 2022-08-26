def get_alivehumans(response):
    items = []
    for item in response['results']:
        if item['status'] == 'Alive' and item['species'] == 'Human':
            char = {
                'id': item['id'],
                'name': item['name'],
                'status': item['status'],
                'species': item['species'],
                'gender': item['gender'],
                'episodes': len(item['episode'])
            }
            items.append(char)

    return items