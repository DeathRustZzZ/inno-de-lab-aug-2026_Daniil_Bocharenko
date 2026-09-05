raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

parts = raw_user_record.split(";")
parts = [part.strip() for part in parts]
user_id = f"UID-{parts[0]}"
user_name = parts[1].replace("_", " ").title()
city = parts[2].upper()
status = parts[3].lower()
normalized_record = " | ".join([user_id, user_name, city, status])
print(f"Нормализованная запись: {normalized_record}")
