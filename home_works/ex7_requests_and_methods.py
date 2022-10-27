import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1
response1 = requests.post(url)
print("#1")
print(response1.text)
print(response1.status_code)

# 2
response2 = requests.head(url, params={"method": "HEAD"})
print("#2")
print(response2.text)
print(response2.status_code)

# 3
response3 = requests.get(url, params={"method": "GET"})
print("#3")
print(response3.text)
print(response3.status_code)

# 4
print("#4", end='\n\n')
methods = ["POST", "GET", "PUT", "DELETE"]
for method in methods:

    get_response = requests.get(url, params={'method': f"{method}"})
    print("GET request")
    print(f"{method} method parameter")
    print(f"Response code: {get_response.status_code}")
    print(f"Response text: {get_response.text}", end='\n\n')

    post_response = requests.post(url, data={'method': f"{method}"})
    print("POST request")
    print(f"{method} method parameter")
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}", end='\n\n')

    put_response = requests.put(url, data={'method': f"{method}"})
    print(f"PUT request")
    print(f"{method} method parameter")
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}", end='\n\n')

    delete_response = requests.delete(url, data={'method': f"{method}"})
    print(f"DELETE request")
    print(f"{method} method parameter")
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}", end='\n\n')
