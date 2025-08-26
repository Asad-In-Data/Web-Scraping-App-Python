import streamlit as st
from scraper import scrape_website

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
          st.success("Scraping successful!")
          st.success("Data scraped successfully!")