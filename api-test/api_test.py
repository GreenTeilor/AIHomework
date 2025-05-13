import requests
import json
from typing import List, Dict, Any

def validate_product(product: Dict[str, Any]) -> List[str]:
    """
    Validate a single product object and return a list of validation errors.
    """
    errors = []
    
    # Validate title
    if not product.get('title') or not isinstance(product['title'], str) or len(product['title'].strip()) == 0:
        errors.append("Empty title")
    
    # Validate price
    price = product.get('price')
    if not isinstance(price, (int, float)) or price < 0:
        errors.append("Negative or invalid price")
    
    # Validate rating
    rating = product.get('rating', {}).get('rate')
    if not isinstance(rating, (int, float)) or rating > 5:
        errors.append("Rating exceeds 5 or is invalid")
    
    return errors

def test_fakestore_api():
    """
    Test the Fake Store API and validate product data.
    """
    # API endpoint
    url = "https://fakestoreapi.com/products"
    
    try:
        # Make GET request
        response = requests.get(url)
        
        # Verify HTTP status code
        if response.status_code != 200:
            print(f"API request failed with status code: {response.status_code}")
            return
        
        # Parse response JSON
        products = response.json()
        
        # Track if any defects were found
        defects_found = False
        
        # Validate each product
        for product in products:
            errors = validate_product(product)
            
            if errors:
                defects_found = True
                print(f"\nDefects found in product (ID: {product.get('id', 'Unknown')}):")
                print(f"Title: {product.get('title', 'N/A')}")
                print("Validation errors:")
                for error in errors:
                    print(f"- {error}")
        
        if not defects_found:
            print("\nNo defects found. All products passed validation.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    print("Starting API validation test...")
    test_fakestore_api() 