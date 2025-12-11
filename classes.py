import sqlite3
from datetime import datetime


class TextMemory:
    def __init__(self, start_id, end_id, db_path="memories.db"):
        self.start_id = start_id
        self.end_id = end_id
        self.db_path = db_path
        self.messages = self._load_messages()
        self.participants = self._get_participants()
        self.title = self._generate_title()

    def _load_messages(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT id, date, name, content 
        FROM messages 
        WHERE id BETWEEN ? AND ? 
        ORDER BY date ASC
        """,
            (self.start_id, self.end_id),
        )

        messages = cursor.fetchall()
        conn.close()
        return messages

    def _get_participants(self):
        # return unique participant names
        return list({msg[2] for msg in self.messages})

    def _generate_title(self):
        if self.messages and len(self.participants) >= 1:
            first_words = (self.messages[0][3] or "")[:30] + "..."
            if len(self.participants) >= 2:
                return f"{self.participants[0]} & {self.participants[1]}: {first_words}"
            return f"{self.participants[0]}: {first_words}"
        return "Empty Memory"

    def get_messages_for_replay(self):
        """Return messages formatted for replay in the UI."""
        return [
            {
                "id": msg[0],
                "date": msg[1],
                "sender": msg[2],
                "content": msg[3],
            }
            for msg in self.messages
        ]

    def __str__(self):
        return f"TextMemory: {self.title} ({len(self.messages)} messages)"


if __name__ == "__main__":
    # Demo / debug usage when running this module directly.
    memory1 = TextMemory(8758, 8800)
    print(memory1)

    for message in memory1.get_messages_for_replay():
        print(f"{message['sender']}: {message['content']}")
