from typing import Optional, Type
import threading

class DatabaseConnection:
    _instance: Optional["DatabaseConnection"] = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls: Type["DatabaseConnection"], *args, **kwargs) -> "DatabaseConnection":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)