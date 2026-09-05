from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    movie_title: str,
    days_overdue: Any,
    fine_rate: float,
) -> tuple[float, float] | None:
    """Calculate the overdue fine and return index for a movie.

    Handles invalid data types, invalid values, and division by zero.

    Args:
        movie_title: Name of the movie.
        days_overdue: Number of overdue days.
        fine_rate: Fine amount charged per overdue day.

    Returns:
        A tuple containing the total fine and return index,
        or None if an error occurs.
    """
    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        return total_fine, return_index

    except TypeError as error:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {error}")

    except ValueError as error:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни "
            f"в число для '{movie_title}': {error}"
        )

    except ZeroDivisionError as error:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки "
            f"для '{movie_title}': {error}"
        )

    finally:
        print("--- Проверка транзакции возврата завершена ---")

    return None


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

result = calculate_overdue_fine("Matrix", 5, 1.5)

if result is not None:
    print(f"Фильм: 'Matrix' | Итоговый штраф: {result[0]}$ | Индекс: {result[1]}")

calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3], 3.0)
