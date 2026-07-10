from langchain_core.tools import tool

schedule = {}

@tool
def add_to_calendar(task: str, date: str) -> str:
    """
    Schedule a task on a particular date.
    Use this tool whenever the user wants to schedule,
    add a reminder or save an event.
    """

    schedule[task] = date

    return f"'{task}' scheduled on {date}"


def show_schedule():
    return schedule