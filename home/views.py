from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('<h1>Hello, Alex</h1>')


def show_details_students(request):
    details_students = {
        'all_students': [
            {
                'first_name': 'George',
                'last_name': 'Popescu',
                'age': 30,
                'is_olympic': False
            },
            {
                'first_name': 'Alex',
                'last_name': 'Gheorghe',
                'age': 36,
                'is_olympic': True
            },
            {
                'first_name': 'Liliana',
                'last_name': 'Filip',
                'age': 36,
                'is_olympic': True
            },
            {
                'first_name': 'Constantin',
                'last_name': 'Rebreanu',
                'age': '38',
                'is_olympic': True
            }
        ]
    }
    return render(request, 'home/details_students.html', details_students)


def show_details_phones(request):
    details_phones = {
        'all_phones': [
            {
                'phone_model': 'Xiaomi',
                'storage_capacity': '256 GB',
                'display_size': '6.7 inch',
                'battery_capacity': '4500 mAh',
                'Google_Services': True
            },
            {
                'phone_model': 'Samsung',
                'storage_capacity': '512 GB',
                'display_size': '6.9 inch',
                'battery_capacity': '4700 mAh',
                'Google_Services': True
            },
            {
                'phone_model': 'Huawei',
                'storage_capacity': '128 GB',
                'display_size': '6.74 inch',
                'battery_capacity': '5000 mAh',
                'Google_Services': False
            }
        ]
    }
    return render(request, 'home/details_phones.html', details_phones)


def show_details_professors(request):
    details_professors = {
        'all_professors': [
            {
                'department': 'History',
                'first_name': 'George',
                'last_name': 'Calinescu'
            },
            {
                'department': 'Mathematics',
                'first_name': 'Mihai',
                'last_name': 'Dumitrescu'
            },
            {
                'department': 'Literature',
                'first_name': 'Lucretia',
                'last_name': 'Puscasu'
            },
            {
                'department': 'Foreign Languages',
                'first_name': 'Gratiela',
                'last_name': 'Olaru'
            }
        ]
    }
    return render(request, 'home/details_professors.html', details_professors)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

