"""
USDA Hardiness Zone API - Basic Usage Example

This example demonstrates the basic usage of the USDA Hardiness Zone API.
API Documentation: https://docs.apiverve.com/ref/hardinesszone
"""

import os
import requests
import json

API_KEY = os.getenv('APIVERVE_API_KEY', 'YOUR_API_KEY_HERE')
API_URL = 'https://api.apiverve.com/v1/hardinesszone'

def call_hardinesszone_api():
    """
    Make a GET request to the USDA Hardiness Zone API
    """
    try:
        # Query parameters
        params &#x3D; {&#x27;zip&#x27;: &#x27;97201&#x27;}

        headers = {
            'x-api-key': API_KEY
        }

        response = requests.get(API_URL, headers=headers, params=params)

        # Raise exception for HTTP errors
        response.raise_for_status()

        data = response.json()

        # Check API response status
        if data.get('status') == 'ok':
            print('✓ Success!')
            print('Response data:', json.dumps(data['data'], indent=2))
            return data['data']
        else:
            print('✗ API Error:', data.get('error', 'Unknown error'))
            return None

    except requests.exceptions.RequestException as e:
        print(f'✗ Request failed: {e}')
        return None

if __name__ == '__main__':
    print('📤 Calling USDA Hardiness Zone API...\n')

    result = call_hardinesszone_api()

    if result:
        print('\n📊 Final Result:')
        print(json.dumps(result, indent=2))
    else:
        print('\n✗ API call failed')
