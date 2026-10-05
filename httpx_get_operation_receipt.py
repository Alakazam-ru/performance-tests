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
create_new_user_date = dict(userId = create_new_user_response_data['user']['id'])

create_credit_card_response = httpx.post(
    url='http://localhost:8003/api/v1/accounts/open-credit-card-account', json=create_new_user_date
    )
create_credit_card_data = create_credit_card_response.json()

create_purchase_operation = {
"status": "IN_PROGRESS",
"amount": 77.99,
"category": "taxi",
"cardId": create_credit_card_data['account']['cards'][0]['id'],
"accountId": create_credit_card_data['account']['id']
}

create_purchase_response = httpx.post(
    url='http://localhost:8003/api/v1/operations/make-purchase-operation', json=create_purchase_operation
    )
create_purchase_data = create_purchase_response.json()

create_receipt_response = httpx.get(f'http://localhost:8003/api/v1/operations/operation-receipt/{create_purchase_data['operation']['id']}')


print("Create deposit data:", create_receipt_response.json())