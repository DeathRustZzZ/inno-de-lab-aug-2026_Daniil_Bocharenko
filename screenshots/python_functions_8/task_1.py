MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0,
) -> tuple[float, bool]:
    # Всю документацию правил через ИИ решил оставить английский для отмосферы международного проекта
    """Calculate the final cost of a rental batch.

    Args:
        quantity: Number of rental discs.
        rental_rate: Rental price per disc.
        discount: Discount as a decimal fraction. Defaults to 0.0.

    Returns:
        A tuple containing the final rental cost and a boolean indicating
        whether the rental batch limit has been exceeded.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


# Позиционные аргументы
batch_1 = calculate_rental_batch(30, 2.99)

# Именованные аргументы
batch_2 = calculate_rental_batch(
    quantity=40,
    rental_rate=4.99,
    discount=0.10,
)

batch_3 = calculate_rental_batch(10, 1.99)

batch_4 = calculate_rental_batch(
    quantity=50,
    rental_rate=3.50,
    discount=0.20,
)


print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
print(
    f"Партия 1 (Academy Dinosaur): Сумма {batch_1[0]}$. Превышение лимита: {batch_1[1]}"
)
print(
    f"Партия 2 (Affair Prejudice): Сумма {batch_2[0]}$. Превышение лимита: {batch_2[1]}"
)
print(f"Партия 3 (Agent Truman): Сумма {batch_3[0]}$. Превышение лимита: {batch_3[1]}")
print(f"Партия 4 (African Egg): Сумма {batch_4[0]}$. Превышение лимита: {batch_4[1]}")
