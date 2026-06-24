from pathlib import Path

SUPPORTED_TYPES = [".txt"]


def load_text_file(file_path: str) -> str:
    """
    Load a text document from disk.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(file_path: str) -> str:
    """
    Generic document loader.
    Future support:
      - PDF
      - DOCX
      - HTML
    """
    path = Path(file_path)

    if path.suffix.lower() not in SUPPORTED_TYPES:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return load_text_file(file_path)


if __name__ == "__main__":
    document_path = "sample.txt"

    try:
        text = load_document(document_path)

        print("=" * 50)
        print(f"Loaded {len(text)} characters")
        print("=" * 50)
        print(text[:500])

    except Exception as e:
        print(f"Error: {e}")