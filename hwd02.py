paragraph = """Python is a high-level, interpreted programming language known for its simplicity and readability."""
length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview (first 50 characters):", paragraph[:50])

replaced_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", replaced_paragraph)

lowercase_paragraph = paragraph.lower()
print("\nLowercase paragraph:\n", lowercase_paragraph)

words = paragraph.split()
print("\nList of words:\n", words)

exist='course' in paragraph.lower()
print(exist)