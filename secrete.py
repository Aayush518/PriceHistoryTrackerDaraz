import secrets

# Generate a random hexadecimal string (e.g., '1a2b3c4d...')
secret_key = secrets.token_hex(16)

# Print the generated secret key
print(secret_key)
