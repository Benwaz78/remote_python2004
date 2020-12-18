from django.shortcuts import render
import requests
q = 'Dog'
url =f'https://pixabay.com/api/?key=18297745-1115a181d3efb2c8c0434064b&q={q}&image_type=photo'
r = requests.get(url).json()
data = {
    'image':r['hits'][0]['webformatURL'],
    'tags': r['hits'][0]['tags']
}
print(data)
def api_data(request):
    q = 'Car'
    url =f'https://pixabay.com/api/?key=18297745-1115a181d3efb2c8c0434064b&q={q}&image_type=photo'
    r = requests.get(url).json()
    data = {
        'image':r['hits'][0]['webformatURL'],
        'tags': r['hits'][0]['tags'],
        'width': r['hits'][0]['webformatWidth'],
        'height': r['hits'][0]['webformatHeight'],
    }
    return render(request, 'frontend/api-data.html', data)
    

