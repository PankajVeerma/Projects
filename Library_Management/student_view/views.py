from django.shortcuts import render
import requests

def home(request):
    try:
        if request.method == 'GET':
            # Fetch data from the API
            response = requests.get("http://127.0.0.1:8000/api/studentapi/")
            
            # Check if the response is valid
            if response.status_code == 200:
                data_format = response.json()  # API should return a list

                # Ensure we pass the full list of books
                if isinstance(data_format, list) and len(data_format) > 0:
                    context = {'books': data_format}  # Correct structure
                else:
                    context = {'books': []}  # Empty list if no data

            else:
                context = {'books': [], 'error': 'Failed to fetch data from API'}

            return render(request, 'home.html', context)

    except requests.exceptions.RequestException as e:
        return render(request, 'home.html', {'books': [], 'error': str(e)})
