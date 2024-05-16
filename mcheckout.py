### 生成checkout页面信息 -- Done

import requests
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

url = "https://api.lemonsqueezy.com/v1/checkouts"

# 确保环境变量已正确设置
api_key = os.getenv("LEMON_SQUEEZY_API_KEY")
if not api_key:
    raise ValueError("LEMON_SQUEEZY_API_KEY environment variable is not set")

store_id = os.getenv("LEMON_SQUEEZY_STORE_ID")
if not store_id:
    raise ValueError("LEMON_SQUEEZY_STORE_ID environment variable is not set")

headers = {
    'Accept': 'application/vnd.api+json',
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f'Bearer {api_key}'
}

data = {
  "data": {
    "type": "checkouts",
    "attributes": {
      "checkout_data": {
        "custom": {
          "user_id": "123",
          "campaign_id": "abc"
        }
      }
    },
    "relationships": {
      "store": {
        "data": {
          "type": "stores",
          "id": store_id  # 使用环境变量中的店铺ID
        }
      },
      "variant": {
        "data": {
          "type": "variants",
          "id": "378532"
        }
      }
    }
  }
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
  print("Checkout created successfully!")
  print(response.json())
else:
  print(f"Error creating checkout: {response.status_code}")
  print(response.text)