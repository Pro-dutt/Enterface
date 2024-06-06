import pandas as pd
import streamlit as st

original_df = pd.read_excel('Bag_of_words/WebsiteCategory.xlsx')
df = pd.DataFrame(original_df, columns=['Name of Website', 'Category'])
website_category = dict(zip(df['Name of Website'], df['Category']))

#url = "ro ce 08a shopify on PR aag wrswess ose ne Discover why millions of entrepreneursx a chose Shopify to build their businessww from hello world to IPO 7 Millions 170 10 44TCrPus Partners Developers CreatorsYour store your way"

#url = "Shopify is the word"
def categorise(url):
     words = url.split()
     st.subheader('Name of the Website and Category:')
     for word in words:
        # Check if the full word is in the website_category dictionary
        if word in website_category:
            st.write(word)
            st.write(website_category[word])
            return
    
        # Check if any combination of words is in the website_category dictionary
        for i in range(len(words)):
            for j in range(i+1, len(words)+1):
                combined_word = ' '.join(words[i:j])
                if combined_word.lower() in website_category:
                    st.write(combined_word)
                    st.write(website_category[combined_word])
                    return
        else:
            continue
            #print(f"No category found for the URL")
