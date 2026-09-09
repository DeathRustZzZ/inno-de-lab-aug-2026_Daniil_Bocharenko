raw_transactions = [
    "SUCCESS:100",
    "FAILED:50",
    "SUCCESS:-10",
    "SUCCESS:0",
    "SUCCESS:250",
    "ERROR:200",
]

# Оставляем только SUCCESS-транзакции
clean_transactions = [
    int(transaction.split(":")[1])
    for transaction in raw_transactions
    if transaction.split(":")[0] == "SUCCESS" and int(transaction.split(":")[1]) > 0
]

print(f"Очищенные транзакции: {clean_transactions}")
