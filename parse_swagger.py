# Install the requests library
# You can install it using: pip install requests
import requests

SWAGGER_URL = "http://petstore.swagger.io"
response = requests.get(SWAGGER_URL)

if response.status_code == 200:
    swagger_data = response.json()
    endpoints = list(swagger_data.get("paths", {}).keys())

    print("Endpoints in Swagger:")
    for endpoint in endpoints:
        print(f'"{endpoint}"')

else:
    print(f"Failed to fetch Swagger JSON. Status Code: {response.status_code}")
