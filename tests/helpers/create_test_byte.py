from src.core.brain_services import BrainServices
from src.core.byte_brain import ByteBrain
from src.core.memory import Memory
from src.core.save_system import SaveSystem


def create_test_byte(memory: Memory | None = None):

    if memory is None:
        memory = Memory()

    services = BrainServices.default()

    return ByteBrain(
        services=services,
        memory=memory,
        save_system=SaveSystem(),
    )