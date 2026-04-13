from core.orchestrator import Orchestrator

def main():
    print("IGRIS is online. Type 'exit' to quit.\n")

    orchestrator = Orchestrator()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("IGRIS shutting down...")
            break

        response = orchestrator.handle(user_input)
        print(f"IGRIS: {response}")

if __name__ == "__main__":
    main()