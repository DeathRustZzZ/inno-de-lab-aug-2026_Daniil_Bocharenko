requested_roles = [
    "guest",
    "developer",
    "guest",
    "admin",
    "developer",
    "guest",
]

required_admin_roles = {
    "admin",
    "security_officer",
    "audit_manager",
}

unique_requested_roles = set(requested_roles)
common_admin_roles = unique_requested_roles & required_admin_roles
missing_admin_roles = required_admin_roles - unique_requested_roles
has_security_officer = "security_officer" in unique_requested_roles

print(f"Уникальные запрошенные роли: {unique_requested_roles}")
print(f"Общие административные роли: {common_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")
