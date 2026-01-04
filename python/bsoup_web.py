import requests
from bs4 import BeautifulSoup

def download_and_strip_css(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove <link> tags for external stylesheets
        for link in soup.find_all('link', rel='stylesheet'):
            link.decompose()

        # Remove <style> tags containing inline CSS
        for style in soup.find_all('style'):
            style.decompose()

        # Remove inline 'style' attributes from all tags
        for tag in soup.find_all(attrs={'style': True}):
            del tag['style']

        return soup.prettify()  # Return cleaned HTML as a string

    except requests.exceptions.RequestException as e:
        print(f"Error downloading content: {e}")
        return None

# Example usage:
url = "https://www.16personalities.com/intp-strengths-and-weaknesses"  # Replace with the desired URL
cleaned_html = download_and_strip_css(url)

if cleaned_html:
    with open("cleaned_output.html", "w", encoding="utf-8") as f:
        f.write(cleaned_html)
    print("HTML content downloaded and CSS stripped successfully.")
else:
    print("Failed to process the URL.")