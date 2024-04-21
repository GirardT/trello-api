from trello_api import get_lists

def list_lists(board_id):
    lists_data = get_lists(board_id)

    for trello_list in lists_data:
        print("List Name:", trello_list['name'])
        print("ID:", trello_list['id'])
        print("-" * 50)

    return lists_data

if __name__ == "__main__":
    board_id = input("Enter the Board ID: ")
    list_lists(board_id)