from pathlib import Path
from tempfile import TemporaryDirectory

from src.core.byte_brain import ByteBrain
from src.core.long_term_memory import LongTermMemory
from src.core.services.brain_services import BrainServices
from src.core.memory import Memory

def main():

    print("=" * 60)
    print("MISSION 094 - BYTE LONG-TERM MEMORY TEST")
    print("=" * 60)

    with TemporaryDirectory() as temp_dir:

        memory_file = Path(temp_dir) / "byte_memory.json"

        long_term_memory = LongTermMemory(
            memory_file
        )
        services = BrainServices.default()
        memory = Memory()

        byte = ByteBrain(
            long_term_memory=long_term_memory,
            services=services,
            memory=memory,
            save_system=None,
)

        # ==================================================
        # REMEMBER
        # ==================================================

        byte.remember_long_term(
            "career",
            "Software Engineering"
        )

        print("🧠 Byte remembers career:")
        print(
            byte.recall_long_term("career")
        )

        assert (
            byte.recall_long_term("career")
            == "Software Engineering"
        )

        print("✅ Byte can remember long-term information.")

        # ==================================================
        # MULTIPLE MEMORIES
        # ==================================================

        byte.remember_long_term(
            "current_skill",
            "Python"
        )

        byte.remember_long_term(
            "learning_goal",
            "Backend Development"
        )

        assert (
            byte.recall_long_term("current_skill")
            == "Python"
        )

        assert (
            byte.recall_long_term("learning_goal")
            == "Backend Development"
        )

        print("✅ Byte can store multiple memories.")

        # ==================================================
        # SEARCH
        # ==================================================

        results = byte.search_long_term("Python")

        assert "current_skill" in results

        print("✅ Byte can search long-term memory.")

        # ==================================================
        # PERSISTENCE
        # ==================================================

        new_memory = LongTermMemory(
            memory_file
        )

        assert (
            new_memory.recall("career")
            == "Software Engineering"
        )

        assert (
            new_memory.recall("learning_goal")
            == "Backend Development"
        )

        print("✅ Byte's long-term memory persists.")

    print()
    print("=" * 60)
    print("✅ Byte Long-Term Memory Test Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()