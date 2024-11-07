import requests
from bs4 import BeautifulSoup
import re
from django.shortcuts import render
from .forms import URLForm

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_emails(html):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, html)
    return set(emails)  # Use a set to remove duplicates

def scrape_emails(request):
    emails = None
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            html = fetch_html(url)
            if html:
                emails = extract_emails(html)

    return render(request, 'Scraper/scrape_emails.html', {'form': form, 'emails': emails})

