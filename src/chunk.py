def chunk_text(text: str, chunk_size: int = 500):
    """
    Split text into chunks.
    """
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


if __name__ == "__main__":
    sample = "This is sample text. " * 100
    chunks = chunk_text(sample)

    print(f"Created {len(chunks)} chunks")