import requests
import json
# целевой URL-адрес
key1='650889ad-e315-4ce5-a923-9bcf7a6a2f06'
key2 = 'rukncn0154'
url = 'https://routing.api.2gis.com/public_transport/2.0?key='+key1
# данные в виде словаря
param = {'some': 'data'}
# кодируем словарь в формат JSON

# отправка POST-запроса с данными в формате JSON
header1 =  {'Content-Type': 'application/json'}
data1 ={
	"locale": "ru",
	"source":
	{
		"name": "Point A",
		"point":
		{
			"lat": 51.734588,
			"lon": 36.149328
		}
	},
	"target":
	{
		"name": "Point B",
		"point":
		{
			"lat": 51.734183,
			"lon": 36.176865
		}
	},
	"transport": ["bus", "tram"]
}
main = {'data':data1,
        'header':header1}
json_param = json.dumps(data1)
resp = requests.post(url, data=json_param)
print(resp)
