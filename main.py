def reversed_words(text: str) -> str:
    """The words of a sentence, last first."""
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    print(reversed_words("one two three"))
