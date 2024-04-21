from list_workspaces import list_workspaces
from list_boards import list_boards
from list_lists import list_lists
from list_cards import list_cards
from list_card_details import list_card_details

# import pprint

def main():
    # List all workspaces and get the workspace ID
    list_workspaces()

    # List all boards within the selected workspace and get the board ID
    workspace_id = input("Enter the Workspace ID: ")
    list_boards(workspace_id)

    # List all lists within the selected board and get the list ID
    board_id = input("Enter the Board ID: ")
    list_lists(board_id)

    # List all cards within the selected list and get the card ID
    list_id = input("Enter the List ID: ")
    list_cards(list_id)

    # Get details of the selected card
    card_id = input("Enter the Card ID: ")
    card_details = list_card_details(card_id)
    # pprint.pprint(card_details)

    return card_details

if __name__ == "__main__":
    main()