
with open(".env") as f:
    for line in f:
        if line.startswith("GOOGLE_API_KEY="):
            google_api_key = line.strip().split("=")[1]
            break

print(google_api_key)




