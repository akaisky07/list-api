import requests

base_url = 'http://127.0.0.1:5000/api/items'

# Function to test GET request for getting the list of items
def test_get_items():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("GET Request - Get Items:")
        print(response.json())
    else:
        print("Error:", response.json())

# Function to test POST request for adding a new item
def test_add_item(name):
    data = {'name': name}
    response = requests.post(base_url, json=data)
    if response.status_code == 201:
        print("POST Request - Add Item:")
        print(response.json())
    else:
        print("Error:", response.json())

if __name__ == '__main__':
    # Test GET request to get the initial list of items
    test_get_items()

    # Test POST request to add a new item
    test_add_item("New Item 1")
    test_add_item("New Item 2")

    # Test GET request to get the updated list of items
    test_get_items()

