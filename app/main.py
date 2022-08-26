from app.model.database import database, insert
from entrypoints.api_requests import get_pages, get_users
from model.user import get_alivehumans

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character/'

data = get_users(baseurl, endpoint, 1)

con = database('rick_and_morty.db')

for items in range(1, get_pages(data) + 1):
    for character in get_alivehumans(get_users(baseurl, endpoint, items)):
        sql = f'INSERT INTO Characters (id, name, status, species, gender, episodes) VALUES ("{character["id"]}", ' \
              f'"{character["name"]}",' \
              f'"{character["status"]}", ' \
              f'"{character["species"]}", ' \
              f'"{character["gender"]}", ' \
              f'"{character["episodes"]}");'
        insert(con, sql)

con.close()
