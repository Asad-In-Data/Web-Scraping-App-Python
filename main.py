import streamlit as st
from bs4 import BeautifulSoup
from scraper import scrape_website

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract data using BeautifulSoup
    data = {
        "title": soup.title.string if soup.title else "No title",
        "headings": [h.get_text() for h in soup.find_all('h1')]
    }
    body = soup.body.get_text() if soup.body else "No body content"
    data["body"] = body
    return data

def clean_data(data):
    # Remove unwanted characters and whitespace
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.strip()
    return data

def display_data(data):
    st.subheader("Scraped Data")
    st.write(f"**Title:** {data['title']}")
    st.write("**Headings:**")
    for heading in data['headings']:
        st.write(f"- {heading}")
    st.write("**Body Content:**")
    st.text(data['body'][:500] + "...")  # Display first 500 characters


def split_text(text, max_length=6000):
    # Split text into chunks of max_length
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# def save_data(data, filename="scraped_data.txt"):
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("Title: " + data['title'] + "\n")
#         f.write("Headings:\n")
#         for heading in data['headings']:
#             f.write("- " + heading + "\n")
#         f.write("Body Content:\n")
#         f.write(data['body'] + "\n")
#     st.success(f"Data saved to {filename}")


st.title("WEB SCRAPER")
url = st.text_input("Enter Website URL to scrape:")
# if url:
#     st.write(f"Scraping {url}...")

if st.button("Start Scraping"):
        st.write("Scraping in progress...")
        result= scrape_website(url)
        if not result:
          st.error("Scraping failed! Possibly blocked or invalid URL.")
        else:
          data = parse_html(result)
          data = clean_data(data)
          st.session_state['data'] = data
          with st.expander("View Scraped Data"):
           display_data(data)
          
        
          st.success("Data scraped successfully!")


st.markdown("---")  
st.markdown(""" 
  <div style="text-align: center;">
    <div style="font-size: 16px; color: #F0EDCC;">
        <p>Made with ❤️ by Asad In Data</p>
        <p> © 2025 Web Scarper App. All rights reserved.</p>
    </div>
  </div>""", unsafe_allow_html=True)

# def save_data(data, filename="scraped_data.txt"):
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("Title: " + data['title'] + "\n")
#         f.write("Headings:\n")
#         for heading in data['headings']:
#             f.write("- " + heading + "\n")
#         f.write("Body Content:\n")
#         f.write(data['body'] + "\n")
#     st.success(f"Data saved to {filename}")
# def main():
#     st.title("Web Scraper")
#     url = st.text_input("Enter URL to scrape:")
#     if st.button("Scrape"):
#         html_content = scrape_website(url)
#         if html_content:
#             data = parse_html(html_content)
#             data = clean_data(data)
#             display_data(data)
#             save_data(data)
#         else:
#             st.error("Failed to retrieve webpage.")

# def run():
#     main()

# def test():
#     assert parse_html("<html><head><title>Test</title></head><body><h1>Heading</h1></body></html>") == {
#         "title": "Test",
#         "headings": ["Heading"],
#         "body": "Heading"
#     }
#     assert clean_data({
#         "title": "  Test  ",
#         "headings": ["  Heading  "],
#         "body": "  Body content  "
#     }) == {
#         "title": "Test",
#         "headings": ["Heading"],
#         "body": "Body content"
#     }
 