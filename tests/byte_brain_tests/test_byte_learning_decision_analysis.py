from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 068 - BYTE LEARNING DECISION ANALYSIS TEST")
    print("=" * 60)

    services = BrainServices.default()
    memory = Memory()
    save_system = SaveSystem()

    byte = ByteBrain(
        services=services,
        memory=memory,
        save_system=save_system,
    )

    print("\n🧠 Your Learning Decision\n")

    print(byte.get_learning_decision())

    print("\n" + "=" * 60)
    print("✅ Byte Learning Decision Analysis Test Completed Successfully!")
    print("=" * 60)