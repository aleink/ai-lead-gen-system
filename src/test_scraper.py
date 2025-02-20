import requests
from bs4 import BeautifulSoup

def main():
    url = "https://example.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract the page title as a simple test
        page_title = soup.title.string if soup.title else "No Title Found"
        print(f"Page Title: {page_title}")
    else:
        print(f"Failed to retrieve {url}, status code: {response.status_code}")

if __name__ == "__main__":
    main()
