import requests
from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest 
from django.core.cache import cache
from . models import City, Ip, Headline
# I Created some views and functions here.

def getHeadlines (searchTerm):
    url_news = 'https://newsapi.org/v2/everything?q={}&from={}&sortBy=popularity&apiKey=70c97d616df84d499c04e8f8b6a39fbd' #how do I make a static final?
    today = datetime.today().strftime('%Y-%m-%d')
    r_news = requests.get(url_news.format(searchTerm, today)).json()
    print ("I GOT NEW NEWS from:" + url_news.format(searchTerm, today))
    hls = min(int(r_news['totalResults']), 6)

    headlines = [ Headline() for i in range(hls)]
    for i in range(hls):
        headline = headlines[i]
        headline.title = r_news['articles'][i]['title'] 
        headline.link = r_news['articles'][i]['url'] 
        headline.source = r_news['articles'][i]['source']['name']
    return headlines

def getWeather(ip):
    url_weather = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e54b61f8809bdf7de465cd779731b86a'
    city = City()
    r_weather = requests.get(url_weather.format(ip.city)).json()
    city.name = ip.city
    city.country_code = ip.country_code
    city.weather_temperature = r_weather['main']['temp']
    city.weather_description = r_weather['weather'][0]['description']
    city.weather_icon = r_weather['weather'][0]['icon']
    return city

def index(request):
    
    ip_in = '64.191.16.50'
    #ip_in = request.META['REMOTE_ADDR'] #one day this will work... 
    
    
    if request.method == 'POST':
        ip_in = request.POST.get("address", "")
 
    print ("processing "+ip_in)
    
    ip = Ip.objects.filter(address=ip_in)
    if not ip:
        url_ip = 'https://api.ipgeolocation.io/ipgeo?apiKey=db119ca8fbde4657b8ee0d8a5f1711e2&ip={}' 
        r_ip = requests.get(url_ip.format(ip_in)).json()
        ip = Ip()
        ip.address = ip_in
        ip.lat = r_ip['latitude']
        ip.long = r_ip['longitude']
        ip.city = r_ip['city']
        ip.state_prov = r_ip['state_prov']
        ip.country = r_ip['country_name']
        ip.country_code = r_ip['country_code2']
        ip.save()
    else:
        ip = ip.get()
        
    cache_key = (ip.city+'-'+ip.country_code).replace(' ','')
    cache_obj = cache.get(cache_key)
    

    if not cache_obj:
        headlines = getHeadlines(ip.city)
        city = getWeather(ip)
        cache_obj = {
            'headlines' : headlines,
            'city' : city,
        }
        cache.set(cache_key, cache_obj, 3600)


    context = {
        'city' : cache_obj['city'],
        'ip_geo' : ip,
        'headlines' : cache_obj['headlines'],
    }
    return render(request, 'ipwn/weather.html', context)
