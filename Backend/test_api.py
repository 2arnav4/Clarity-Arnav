import requests
import json

# Base URL of your Flask backend
BASE_URL = "http://127.0.0.1:5000/api"

def test_verify_news():
    url = f"{BASE_URL}/news/verify"
    payload = {
        "text": "Breaking: Aliens spotted in New York!"  # Example news text
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ /verify endpoint success!")
            print("Response:", json.dumps(response.json(), indent=2))
        else:
            print(f"❌ /verify failed with status code {response.status_code}")
    except Exception as e:
        print(f"❌ /verify endpoint error: {e}")

def test_other_endpoint():
    # Example template for any additional endpoints
    url = f"{BASE_URL}/other_endpoint"
    payload = {"key": "value"}  # Change this
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ /other_endpoint success!")
            print("Response:", json.dumps(response.json(), indent=2))
        else:
            print(f"❌ /other_endpoint failed with status code {response.status_code}")
    except Exception as e:
        print(f"❌ /other_endpoint error: {e}")

if __name__ == "__main__":
    print("Starting API tests...\n")
    test_verify_news()
    # Add more test calls here if you have more endpoints
    # test_other_endpoint()
