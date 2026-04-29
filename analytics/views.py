import json
import os
from django.shortcuts import render
from django.http import JsonResponse

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'mock_data.json')

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def dashboard(request):
    data = load_data()
    context = {
        'data_json': json.dumps(data, ensure_ascii=False),
        'college': data['college_info'],
        'instagram': data['instagram'],
        'gis2': data['gis2'],
        'competitors': data['competitors'],
        'recommendations': data['recommendations'],
    }
    return render(request, 'analytics/dashboard.html', context)

def api_data(request):
    data = load_data()
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
