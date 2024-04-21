from passwords import TRELLO_API
import requests

API_KEY = TRELLO_API["API_KEY"]
TOKEN = TRELLO_API["TOKEN"]

def get_workspaces():
    url = f'https://api.trello.com/1/members/me/organizations?key={API_KEY}&token={TOKEN}'
    response = requests.get(url)
    return response.json()

def get_boards(workspace_id):
    url = f'https://api.trello.com/1/organizations/{workspace_id}/boards?key={API_KEY}&token={TOKEN}'
    response = requests.get(url)
    return response.json()

def get_lists(board_id):
    url = f'https://api.trello.com/1/boards/{board_id}/lists?key={API_KEY}&token={TOKEN}'
    response = requests.get(url)
    return response.json()

def get_cards(list_id):
    url = f'https://api.trello.com/1/lists/{list_id}/cards?key={API_KEY}&token={TOKEN}&attachments=cover'
    response = requests.get(url)
    return response.json()

def get_card_details(card_id):
    url = f'https://api.trello.com/1/cards/{card_id}?key={API_KEY}&token={TOKEN}&attachments=cover'
    response = requests.get(url)
    return response.json()

def get_checklists(card_id):
    url = f'https://api.trello.com/1/cards/{card_id}/checklists?key={API_KEY}&token={TOKEN}'
    response = requests.get(url)
    return response.json()