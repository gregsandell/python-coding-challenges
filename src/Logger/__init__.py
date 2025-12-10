from datetime import datetime

def timestamp() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

class Logger:
    def __init__(self):
        self.entries: list[dict[str, str]] = []

    def log(self, message: str, level: str = "INFO") -> None:
        self.entries.append({
            "message": message,
            "level": level,
            "timestamp": timestamp()
        })

    def get_logs(self) -> list[dict]:
        return self.entries

    def search(self, keyword: str = "", field: str = "message") -> list[dict]:
        if not keyword:
            return self.entries

        if field not in {"message", "level"}:
            raise ValueError(f"Invalid field: {field}")

        return [obj for obj in self.entries if keyword in obj.get(field, "")]


