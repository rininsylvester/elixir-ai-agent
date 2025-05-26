from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def greeting(name:str)->str:
    """Useful while greeting the user"""
    print("Custom tool function has been used")
    return f"Hello {name} , What can I do for you today ?"

def main():
    model = ChatOpenAI(temperature=0)
    tools = [greeting]
    agent_executor = create_react_agent(model , tools)

    print("Welcome ! I am Elixir , your personal AI assistant ")
    print("You can ask me any questions / type 'quit' to exit")

    while True:

        user_input = input("\nUser:").strip()
        
        if user_input == "quit":
            break

        print("\nElixir:" , end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk ["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content , end="")
        print()

if __name__ == "__main__":
    main()