from list_workspaces import list_workspaces
from list_boards import list_boards
from list_lists import list_lists
from list_cards import list_cards
from list_card_details import list_card_details

import pprint

import pandas as pd

def main():
    # List all workspaces and get the workspace ID
    list_workspaces()

    # List all boards within the selected workspace and get the board ID
    workspace_id = input("Enter the Workspace ID: ")
    list_boards(workspace_id)

    # List all lists within the selected board and get the list ID
    board_id = input("Enter the Board ID: ")

    all_cards = list()

    for lista in list_lists(board_id):
        cards = list_cards(lista['id'])
        for card in cards:
            new_card = (lista['name'], card['name'])
            all_cards.append(new_card)

    df = pd.DataFrame(all_cards)
    print(df)

    # Export DataFrame to Excel file
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
    excel_file = "all_trello_cards.xlsx"
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f"Exported Trello cards to {excel_file}")

if __name__ == "__main__":
    main()