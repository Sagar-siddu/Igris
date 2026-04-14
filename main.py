from core.agent import Agent

def main():
    agent = Agent()

    print("IGRIS LLM Test Mode (type 'exit' to quit)\n")

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = agent.run(messages)

        if isinstance(response, dict):
            if response.get("type") == "response":
                print("IGRIS:", response.get("content"))
            elif response.get("type") == "tool":
                print("IGRIS (tool decision):", response)
        else:
            print("IGRIS:", response)

        messages.append({
            "role": "assistant",
            "content": str(response)
        })

if __name__ == "__main__":
    main()