
import requests

url = "https://text-in-images-recognition.p.rapidapi.com/prod"

payload = { "objectUrl": "https://qph.cf2.quoracdn.net/main-qimg-9afe7ad38afd25817fc83e85fe149a75.webp" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "1e8b8fc25bmsh37e839b21d396d1p1adea0jsn09ee2d22084b",
	"X-RapidAPI-Host": "text-in-images-recognition.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()) 