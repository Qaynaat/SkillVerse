import json
from pathlib import Path


class LongTermMemory:
    """
    Mission 094

    Persistent long-term memory for SkillVerse.

    Stores important learner information that should survive
    beyond the current conversation/session.
    """

    def __init__(self, file_path="data/long_term_memory.json"):
        self.file_path = Path(file_path)
        self.memory = {}

        self._ensure_storage()
        self._load()

    # ==========================================================
    # STORAGE
    # ==========================================================

    def _ensure_storage(self):
        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file_path.exists():
            self._save()

    def _load(self):
        try:
            with self.file_path.open(
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.memory = data
            else:
                self.memory = {}

        except (json.JSONDecodeError, OSError):
            self.memory = {}

    def _save(self):
        with self.file_path.open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                self.memory,
                file,
                indent=4,
                ensure_ascii=False
            )

    # ==========================================================
    # REMEMBER
    # ==========================================================

    def remember(self, key, value):
        """
        Store important learner information.

        Returns True when the information is stored.
        """

        if not key:
            raise ValueError("Memory key cannot be empty.")

        self.memory[str(key)] = value
        self._save()

        return True

    # ==========================================================
    # RECALL
    # ==========================================================

    def recall(self, key, default=None):
        """
        Retrieve previously stored information.
        """

        return self.memory.get(
            str(key),
            default
        )

    # ==========================================================
    # UPDATE
    # ==========================================================

    def update(self, key, value):
        """
        Update an existing memory item.

        Unlike remember(), update() requires
        the memory to already exist.
        """

        key = str(key)

        if key not in self.memory:
            return False

        self.memory[key] = value
        self._save()

        return True

    # ==========================================================
    # FORGET
    # ==========================================================

    def forget(self, key):
        """
        Remove one memory item.
        """

        key = str(key)

        if key not in self.memory:
            return False

        del self.memory[key]
        self._save()

        return True

    # ==========================================================
    # SEARCH
    # ==========================================================

    def search(self, query):
        """
        Search memory keys and values.
        """

        if not query:
            return {}

        query = str(query).lower()

        results = {}

        for key, value in self.memory.items():

            searchable_key = str(key).lower()
            searchable_value = str(value).lower()

            if (
                query in searchable_key
                or query in searchable_value
            ):
                results[key] = value

        return results

    # ==========================================================
    # GET ALL
    # ==========================================================

    def get_all(self):
        """
        Return a copy of all long-term memory.
        """

        return dict(self.memory)

    # ==========================================================
    # CLEAR
    # ==========================================================

    def clear(self):
        """
        Clear all long-term memory.
        """

        self.memory.clear()
        self._save()

        return True