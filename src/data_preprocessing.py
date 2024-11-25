from bs4 import BeautifulSoup
from bs4.element import Comment
import html

def html_escape(html_content):
     # convert to HTML-safe sequence
    res = html.escape(html_content, quote=True)
    return res

# return if a html tag contains visible data (useful article content)
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# get only the article content from the html web scraped information
def get_article_content(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

# get the page content from the URL
def get_page_content(page):
    try:
        page = get_article_content(page)
        page = html_escape(page)
        page = page.replace("\n", "")
        page = page.strip()
    except:
        return '""'
    return '"' + page + '"'

def data_preprocessing(article_content, article_title):
    page = get_page_content(article_content)
    if page.strip() == '""':
        return '"' + article_title + '"'
    else:
       return page