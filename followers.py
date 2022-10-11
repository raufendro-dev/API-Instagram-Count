#import

import  requests
from bs4 import BeautifulSoup

def followers(username):
    Source_html = 'https://www.picuki.com/profile/'+username
    page = requests.get(Source_html)
    Soup_obj = BeautifulSoup(page.text, 'html.parser')
    # Find all the elements CSS selector
    elements = Soup_obj.select('.followed_by')
    # prints all elements under that tag
    #To find the content of the element
    for ele in elements:
        hasil = ele.string
        return hasil

def profile(username):
    Source_html = 'https://www.picuki.com/profile/'+username
    page = requests.get(Source_html)
    Soup_obj = BeautifulSoup(page.text, 'html.parser')
    # Find all the elements CSS selector
    elements = Soup_obj.select('.profile-avatar-image')
    # prints all elements under that tag
    #To find the content of the element
    for ele in elements:
        hasil = ele['src']
        return hasil

def filejson(username):
    hasil = followers(username)
    gambar = profile(username)
    if hasil is None:
        return {'error':'user privat atau user tidak ditemukan'}
    else:
        api = { 'username':username, 'followers':hasil, 'fotoprofil':gambar, 'author':'raufendro-dev'}
        return api
            
