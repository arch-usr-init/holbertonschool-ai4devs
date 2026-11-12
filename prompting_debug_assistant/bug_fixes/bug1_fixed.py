"""Sum positive integers from a comma-separated string."""


def sum_positive(csv_text):
    total = 0
    for part in csv_text.split(","):
        part = part.strip()
        if not part:
            continue
        number = int(part)
        if number > 0:
            total += number
    return total


def main():
    sample = "3, -2, 5, 0"
    print("Positive sum:", sum_positive(sample))


if __name__ == "__main__":
    main()
