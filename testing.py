import requests

url = 'http://127.0.0.1:5000/'  # localhost and the defined port + endpoint


def test_home():
    print("Testing home")
    response = requests.get(url)
    print(response.json())


def test_highlight():
    print("Testing highlight")
    response = requests.get(url+"highlight")
    print(response.json())

def test_news():
    print("Testing news")
    response = requests.get(url+"newsitem/marraskuu/3")
    print(response.json())


test_home()
test_news()
test_highlight()





