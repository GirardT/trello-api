from trello_api import get_boards

def list_boards(workspace_id):
    boards_data = get_boards(workspace_id)

    for board in boards_data:
        print("Board Name:", board['name'])
        print("ID:", board['id'])
        print("-" * 50)

    return boards_data

if __name__ == "__main__":
    workspace_id = input("Enter the Workspace ID: ")
    list_boards(workspace_id)