from typing import Type, List
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from superagi.helper.trello_create_task import TrelloAddTaskWrap
from superagi.config.config import get_config


class TrelloAddTaskSchema(BaseModel):
    task_name: str=Field(..., description="Task name to create new task on Trello")
    task_due_date: str=Field(..., description="Task due date for the new task ,Use the format 'YYYY-MM-DD' in str")

class TrelloAddTaskTool(BaseTool):
    name="TrelloAddTask"
    description = (
        "A tool to create a new task on Trello with a specified due date."
        "Inputs should be task new name and task due date in YYYY-MM-DD format."
    )

    def _execute(self,task: TrelloAddTaskSchema):
        trello_API_KEY=get_config("TRELLO_API_KEY")
        trello_API_Token=get_config("TRELLO_API_TOKEN")
        board_id="647bb5afdb469926509efdb0"
        task_name=task.task_name
        task_due_date=task.task_due_date
        
        print(f"Task Name: {task_name}, Task_due_date: {task_due_date}")

        trello_add_task=TrelloAddTaskWrap(trello_API_KEY,trello_API_Token,board_id)
        result=trello_add_task.add_new_task(task_name,task_due_date)

        return result


