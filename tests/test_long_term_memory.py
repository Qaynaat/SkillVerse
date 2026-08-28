from pathlib import Path
from tempfile import TemporaryDirectory

from src.core.long_term_memory import LongTermMemory


def main():

    print("=" * 60)
    print("MISSION 094 - LONG-TERM MEMORY TEST")
    print("=" * 60)

    with TemporaryDirectory() as temp_dir:

        memory_file = Path(temp_dir) / "memory.json"

        memory = LongTermMemory(memory_file)

        # ==================================================
        # REMEMBER
        # ==================================================

        assert memory.remember(
            "career",
            "Software Engineering"
        )

        assert memory.recall("career") == "Software Engineering"

        print("✅ Memory recording works.")

        # ==================================================
        # MULTIPLE MEMORIES
        # ==================================================

        memory.remember(
            "current_skill",
            "Python"
        )

        memory.remember(
            "learning_goal",
            "Become a Backend Developer"
        )

        print("✅ Multiple memories work.")

        # ==================================================
        # UPDATE
        # ==================================================

        assert memory.update(
            "current_skill",
            "Python Programming"
        )

        assert memory.recall(
            "current_skill"
        ) == "Python Programming"

        print("✅ Memory update works.")

        # ==================================================
        # SEARCH
        # ==================================================

        results = memory.search("Python")

        assert "current_skill" in results

        print("✅ Memory search works.")

        # ==================================================
        # PERSISTENCE
        # ==================================================

        new_memory = LongTermMemory(memory_file)

        assert new_memory.recall(
            "career"
        ) == "Software Engineering"

        assert new_memory.recall(
            "learning_goal"
        ) == "Become a Backend Developer"

        print("✅ Memory persistence works.")

        # ==================================================
        # FORGET
        # ==================================================

        assert new_memory.forget(
            "learning_goal"
        )

        assert new_memory.recall(
            "learning_goal"
        ) is None

        print("✅ Forget operation works.")

        # ==================================================
        # GET ALL
        # ==================================================

        all_memory = new_memory.get_all()

        assert "career" in all_memory
        assert "current_skill" in all_memory

        print("✅ Get-all operation works.")

        # ==================================================
        # CLEAR
        # ==================================================

        assert new_memory.clear()

        assert new_memory.get_all() == {}

        print("✅ Clear operation works.")

    print()
    print("=" * 60)
    print("✅ Long-Term Memory Test Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()