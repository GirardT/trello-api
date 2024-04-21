from trello_api import get_cards

def list_cards(list_id):
    cards_data = get_cards(list_id)

    for card in cards_data:
        print("Card Name:", card['name'])
        print("ID:", card['id'])
        print("-" * 50)

    return cards_data

if __name__ == "__main__":
    list_id = input("Enter the List ID: ")
    list_cards(list_id)