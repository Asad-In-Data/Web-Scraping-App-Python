import streamlit as st

st.title("WEB SCRAPER")
url = st.text_input("Enter Website URL to scrape:")
# if url:
#     st.write(f"Scraping {url}...")
if st.button("Start Scraping"):
        st.write("Scraping in progress...")
        # Placeholder for scraping logic
        st.write("Scraping completed!")
        st.success("Data scraped successfully!")