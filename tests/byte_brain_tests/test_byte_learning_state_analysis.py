from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 069 - BYTE LEARNING STATE ANALYSIS TEST")
    print("=" * 60)

    services = BrainServices.default()
    memory = Memory()
    save_system = SaveSystem()

    byte = ByteBrain(
        services=services,
        memory=memory,
        save_system=save_system,
    )

    print("\n🧠 Your Learning State\n")

    print(byte.get_learning_state())

    print("\n" + "=" * 60)
    print("✅ Byte Learning State Analysis Test Completed Successfully!")
    print("=" * 60)