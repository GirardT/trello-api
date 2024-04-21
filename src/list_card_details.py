from trello_api import get_card_details, get_checklists

def list_card_details(card_id):
    card_data = get_card_details(card_id)

    print("Card Name:", card_data['name'])
    print("Card Description:", card_data['desc'])
    print("Card URL:", card_data['url'])

    if card_data['attachments']:
        print("\n\nATTACHMENTS:")

        for attachment in card_data['attachments']:
            print("\nName:", attachment['name'])
            print("URL:", attachment['url'])

    checklists_data = get_checklists(card_id)

    if checklists_data:
        print("\n\nCHECKLISTS:")

        for checklist in checklists_data:
            print("\n"+checklist['name'])
            for item in checklist['checkItems']:
                print(f"{'✅' if item['state'] == 'complete' else '☐ '}{item['name']}")
    
    return card_data, checklists_data

if __name__ == "__main__":
    card_id = input("Enter the Card ID: ")
    list_card_details(card_id)