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
create_new_user_deposit_date = dict(userId = create_new_user_response_data['user']['id'])

print("Create user response:", create_new_user_response.status_code, end='\n')
print("Created user data:",create_new_user_response_data, end='\n')

get_new_user = httpx.post(
    url='http://localhost:8003/api/v1/accounts/open-deposit-account', json=create_new_user_deposit_date
    )
print("Create deposit response:", get_new_user.status_code, end='\n')
print("Create deposit data:", get_new_user.json())