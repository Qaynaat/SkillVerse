from src.core.memory import Memory

memory = Memory()

memory.add_message("User", "Hello Byte!")
memory.add_message("Byte", "Hello! Nice to meet you.")

memory.add_message("User", "Tell me about Software Engineering")
memory.add_message("Byte", "Software Engineering is...")

print("=" * 60)
print("BYTE CONVERSATION HISTORY")
print("=" * 60)
print()

history = memory.get_history()

for speaker, message in history:
    print(f"{speaker}:")
    print(message)
    print()

print("=" * 60)
print("Total Messages:", len(history))
print("=" * 60)