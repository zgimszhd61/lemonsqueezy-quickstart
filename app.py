from dotenv import load_dotenv
import os
load_dotenv()
import requests

# print(os.getenv("LEMON_SQUEEZY_API_KEY"))

ApiEndpoint = "https://api.lemonsqueezy.com/v1/"
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {os.getenv("LEMON_SQUEEZY_API_KEY")}',
}

# data = {
#         'license_key': license_key,
#         'instance_name': instance_name,
# }

print(headers)


#### https://api.lemonsqueezy.com/v1/licenses/activate

#### https://api.lemonsqueezy.com/v1/license-keys/{license_id}