from trello_api import get_workspaces

def list_workspaces():
    workspaces_data = get_workspaces()

    for workspace in workspaces_data:
        print("Workspace:", workspace['displayName'])
        print("ID:", workspace['id'])
        print("-" * 50)

    return workspaces_data

if __name__ == "__main__":
    list_workspaces()