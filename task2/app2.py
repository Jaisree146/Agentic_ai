from agent import PlanningAgent
from security import Security
import time
import traceback

agent = PlanningAgent()
security = Security()

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    if not security.check_prompt(question):
        print("Prompt Injection Detected")
        continue

    start = time.time()
    try:
        answer = agent.ask(question)
        elapsed = time.time() - start
        print(f"\nAssistant (response time: {elapsed:.2f}s):")
        print(answer)
    except Exception as e:
        elapsed = time.time() - start
        print(f"\nError after {elapsed:.2f}s: {e}")
        traceback.print_exc()