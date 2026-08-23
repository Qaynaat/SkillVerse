from src.core.byte_brain import ByteBrain
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory
from src.core.save_system import SaveSystem


if __name__ == "__main__":

    print("=" * 60)
    print("MISSION 070 - BYTE LEARNER PROFILE SNAPSHOT TEST")
    print("=" * 60)

    # ==================================================
    # Create Byte dependencies
    # ==================================================

    services = BrainServices.default()
    memory = Memory()
    save_system = SaveSystem()

    # ==================================================
    # Create ByteBrain
    # ==================================================

    byte = ByteBrain(
        services=services,
        memory=memory,
        save_system=save_system,
    )

    # ==================================================
    # Verify service connection
    # ==================================================

    assert hasattr(
        byte,
        "learner_profile_snapshot"
    )

    assert (
        byte.learner_profile_snapshot
        is services.learner_profile_snapshot
    )

    # ==================================================
    # Generate Byte's snapshot
    # ==================================================

    print("\n🧠 Your Learner Profile Snapshot\n")

    response = byte.get_learner_profile_snapshot()

    print(response)

    # ==================================================
    # Basic output verification
    # ==================================================

    assert response is not None
    assert isinstance(response, str)

    assert "Learner Profile Snapshot" in response
    assert "Learning State" in response
    assert "Risk" in response
    assert "Performance" in response
    assert "Velocity" in response
    assert "Primary Intervention" in response
    assert "Learning Decision" in response
    assert "Next Best Action" in response
    assert "Overall Priority" in response

    print("\n" + "=" * 60)
    print(
        "✅ Byte Learner Profile Snapshot Test "
        "Completed Successfully!"
    )
    print("=" * 60)