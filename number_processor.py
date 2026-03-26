def process_numbers(numbers):
    filtered_numbers = filter(lambda x: x >= 1, numbers)

    processed_numbers = map(lambda x: x * 2 if x % 2 == 0 else x * 3, filtered_numbers)
    return list(processed_numbers)