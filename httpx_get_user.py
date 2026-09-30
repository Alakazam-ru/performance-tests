import time
import httpx

create_new_user = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_new_user_response = httpx.post(url='http://localhost:8003/api/v1/users', json=create_new_user)
create_new_user_response_data = create_new_user_response.json()

print(create_new_user_response.status_code)
print(create_new_user_response_data)

get_new_user = httpx.get(f"http://localhost:8003/api/v1/users/{create_new_user_response_data['user']['id']}")

print("Get user response:", get_new_user.json())
print("Status Code:", get_new_user.status_code)