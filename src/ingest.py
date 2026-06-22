from pathlib import Path


def load_text_file(file_path: str) -> str:
    """
    Load a text document from disk.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    text = load_text_file("sample.txt")
    print(text[:500])