import time
from collections.abc import Callable
from typing import Any

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Measure and log the execution time of a function.

    Args:
        func: Function whose execution time should be measured.

    Returns:
        A wrapper function that executes the original function,
        logs its execution time, and returns the original result.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        execution_time = time.perf_counter() - start_time

        print(
            f"{PERFORMANCE_LOG_PREFIX} "
            f"Функция '{func.__name__}' выполнена "
            f"за {round(execution_time, TIME_DECIMALS)} сек."
        )

        return result

    return wrapper


@performance_logger
def get_sorted_report(
    sales_data: list[dict[str, str | float]],
) -> list[dict[str, str | float]]:
    # Всю документацию правил через ИИ решил оставить английский для отмосферы международного проекта
    """Sort genre revenue data by total sales in descending order.

    Args:
        sales_data: List of dictionaries containing category names
            and their total sales.

    Returns:
        A new list sorted by total_sales in descending order.
    """
    return sorted(
        sales_data,
        key=lambda item: item["total_sales"],
        reverse=True,
    )


sales_data_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55},
]

sales_data_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00},
]

sales_data_3 = [
    {"category": "Drama", "total_sales": 500.00},
]


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

print("--- ТЕСТ 1 ---")
report_1 = get_sorted_report(sales_data_1)

print("Топ категорий по выручке:")
for index, item in enumerate(report_1, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 2 ---")
report_2 = get_sorted_report(sales_data_2)

print("Топ категорий по выручке:")
for index, item in enumerate(report_2, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 3 ---")
report_3 = get_sorted_report(sales_data_3)

print("Топ категорий по выручке:")
for index, item in enumerate(report_3, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")
