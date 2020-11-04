import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "petal_length": 4,
    "sepal_length": 4,
    "petal_width": 1,
    "sepal_width": 2
}
response = requests.post(url, data=body)
print(response.json())

def test_petal():
    print("Test petal")
    assert response.json() == "iris-setosa" or "iris-versicolor" or 'iris-virginica'
