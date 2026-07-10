from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from calendar_tool import add_to_calendar

class PlanningAgent:

    def __init__(self):

        self.model = ChatOllama(
            model="qwen2.5"     
        )

        self.agent = create_agent(
            model=self.model,
            tools=[add_to_calendar],
            system_prompt="""
You are an AI Planning Assistant.

Responsibilities

1. Break goals into tasks.
2. Update plans.
3. If user asks to schedule or add reminders,
   ALWAYS call the add_to_calendar tool.

Never pretend to schedule.
Always use the tool.
"""
        )

    def ask(self, message):

        response = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )

        return response["messages"][-1].content