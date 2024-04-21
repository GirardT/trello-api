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

```plaintext
Card Name: If I Wanted to Go From Broke to Millionaire, Here’s What I’d Do
Card Description: 
Card URL: https://trello.com/c/e2oAyvB3/476-if-i-wanted-to-go-from-broke-to-millionaire-heres-what-id-do

ATTACHMENTS:

Name: https://www.youtube.com/watch?v=m3ytRbIzsWM
URL: https://www.youtube.com/watch?v=m3ytRbIzsWM

Name: Build a 6 Figure Skill
URL: https://trello.com/1/cards/66249ca41a20bd8a3d4a1e18/attachments/66249d2fc7d3c0b6ee066391/download/image.png

Name: F.O.C.U.S.
URL: https://trello.com/1/cards/66249ca41a20bd8a3d4a1e18/attachments/66249db05a1631aa2010bb4f/download/image.png

... (Additional attachments)

CHECKLISTS:

Checklist
☐ Build a 6 Figure Skill
☐ F.O.C.U.S.
☐ Friend-ventory
☐ Time Assassins
☐ Feed Your Mind
☐ Achievement Roadmap Process, Attraction Velocity
☐ Trade Money for Money

Feed Your Mind - Which books?
☐ Top 5 books in *<insert topic>*
☐ Top 150 books influenced by *<insert title of the book from the top 5 books>*
☐ Books will give you frameworks to feed your mind to improve your skills
```
