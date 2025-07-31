# Introduction

# https://en.wikipedia.org/wiki/Python_(programming_language)

import requests

# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# response = requests.get(url)

# if response.status_code == 200:
#     print(response.text[:500])
# else:
#     print(f"Failed to retreive data. Status Code: {response.status_code}")

# from bs4 import BeautifulSoup

# html_content = "<h1>Main Tittle</h1> <p>This is a sample paragraph</p> <a href='https://example.com'>Click Here</a>"
# soup = BeautifulSoup(html_content, "html.parser")

# print(soup.h1.text)
# print(soup.p.text)
# print(soup.a.text)
# print(soup.a.href)


# Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup

# Step 1: Get Wikipedia Article Url
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retreive data. Status Code: {response.status_code}")
        return None
    
# Step 2: Extrack Article Title
def get_article_title(soup):
    return soup.find('h1').text

# Step 3: Extrack Article Summary
def get_article_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No Summary Found"

# Step 4: Extrack Headings
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

# Step 5: Extrack Related Links
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('wiki') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))[:5]


# Step 6: Main Program
def main():
    topic = input("Enter a topic to search on Wikipedia: ").strip()
    page_content = get_wikipedia_page(topic)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)
        
        print("\n----- Wikipedia Article Details -----")
        print(f"\nTittle: {title}") 
        print(f"\nSummary: {summary}") 
        print(f"\nSummary:") 
        for heading in headings[:5]:
            print("- " + heading)
            
        print("\nRelated Links:")
        for link in related_links:
            print("-" + link)
            
# Run Program
if __name__ == "__main__":
    main()