import requests

url = "https://www.nike.com/kr/launch/?type=upcoming"
header={"Accept-Encoding": "gzip", "Content-Type":"application/json"}
response=requests.get(url, headers=header)
print(response.text)