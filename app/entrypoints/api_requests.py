import requests


def get_users(baseurl, endpoint, number):
    r = requests.get(baseurl + endpoint + f'?page={number}')
    return r.json()


def get_pages(response):
    return response['info']['pages']