import requests

class TrelloAddTaskWrap:

    def __init__(self,trello_API_KEY,trello_API_Token,board_id) -> None:
        self.trello_API_KEY=trello_API_KEY;
        self.trello_API_Token=trello_API_Token
        self.board_id=board_id

    def add_new_task(self,task_name,task_due_date):
        trello_url=f"https://api.trello.com/1/cards?key={self.trello_API_KEY}&token={self.trello_API_Token}"
        
        payload = {
        "name": task_name,
        "idList": self.board_id,
        "due": task_due_date,
        }

        response = requests.post(trello_url, data=payload)
        
        if response.status_code == 200:
            return "Task created successfully!"
        else:
            return "Error creating task."

