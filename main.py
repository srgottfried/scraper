from WebScraper import WebScraper

url = "https://arxiv.org/abs/2304.04947"

ws = WebScraper(url)

print(ws.get_title)
print(ws.get_description)