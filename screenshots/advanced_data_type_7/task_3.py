db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres",
    }
}

connection = db_config.get("connection", {})
host = connection.get("host", "")
port = connection.get("port", 0)

ssl_mode = db_config.get("ssl_settings", {}).get(
    "ssl_mode",
    "verify-full",
)

connection["user"] = "admin"

connection["max_connections"] = 100

print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")

for key, value in connection.items():
    print(f"* {key}: {value}")
