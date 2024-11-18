#!/usr/bin/python
import requests
import re

def fetch_telegraph_content(page_path):
    url = f"https://api.telegra.ph/getPage/{page_path}?return_content=true"
    response = requests.get(url)
    return response.json()

def fetch_telegraph_views(page_path):
    url = f"https://api.telegra.ph/getViews/{page_path}"
    response = requests.get(url)
    return response.json()

def list_telegraph_images(page_path):
    url = f"https://api.telegra.ph/getPage/{page_path}?return_content=true"
    data = requests.get(url)
    try:
        # Fetch the page content
        response = requests.get(url)
        print(response.status_code)
        
        # Parse the JSON response
        data = response.json()
        if 'result' in data and 'content' in data['result']:
            content = data['result']['content']
            # Extract image URLs
            image_urls = []
            for item in content: 
                if item.get('tag') == 'figure' and 'children' in item:
                    for mychild in item['children']:
                        if mychild.get('tag')=='img' and 'attrs' in mychild:
                            image_urls.append(mychild['attrs']['src'])
            return image_urls
        else:
            print("No valid content found in the response.")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    return []

def fetch_image(fname,link):
    response = requests.get(link)
    data = response.content
    f = open(fname,'wb')
    f.write(data)
    f.flush()
    f.close()
    return 0
