# Trello API Python Script

This Python script provides functionalities to interact with the Trello API. It allows you to list workspaces, boards, lists, and cards, and retrieve detailed information about specific cards in a clear and organised manner.

## Project Structure

The project is organised into the following files:

- `__init__.py`: Initialises the package and defines the modules to be imported.
- `trello_api.py`: Contains functions to interact with the Trello API.
- `list_workspaces.py`: Lists all Trello workspaces and their IDs.
- `list_boards.py`: Lists all boards within a selected workspace and their IDs.
- `list_lists.py`: Lists all lists within a selected board and their IDs.
- `list_cards.py`: Lists all cards within a selected list and their IDs.
- `list_card_details.py`: Retrieves detailed information about a specific card, including attachments and checklists, displayed in a pretty and easy-to-read format.

### Retrieve Detailed Card Information

The `list_card_details.py` module provides a comprehensive view of specific cards. When you select a card by its ID, the script presents its details in a structured format:

- **Card Name**: Displays the name of the card.
- **Card Description**: Shows the description of the card.
- **Card URL**: Provides the URL link to the card on Trello.

#### Attachments

If the card has attachments, the script lists them with their names and URLs, making it easy to access any linked files or images.

#### Checklists

The script also fetches and displays any checklists associated with the card. Each checklist item is presented with a checkbox indicating its completion status, allowing you to quickly see what tasks have been completed and what's pending.

