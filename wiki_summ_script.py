# NLTK Tutorial: https://www.youtube.com/watch?v=dFe7tbH39Eg
# This program is designed to take an input topic, scrape the Wikipedia page, and summarize the text using NLTK.
# Eventually this will be run as a Discord bot, but one step at a time!

# ----------
# Pseudocode:
# ---
# 1. Take input text
#     1a? First ask for category, use as additional search parameter (e.g., film)
#     1b. OR design the bot as a film searcher and just use film in every search
# 2. Open selenium
# 3. navigate to wikipedia
# 4. search input_text + input_category
# 5. return top 3 categories
#     5a. wait for input - select category
# 6. Navigate to specified page
# 7. Scrape page
#     7a. Remove superfluous content, e.g., header, sidebar, sources, etc.
# 8. Page scrapings becomes website_text_input
# 9. Summarize using NLTK *(See video link at top)*
# 10. Return summary
# 11. Every 10th use, ask for feedback? (simple number ranking)
# 12. send feedback to a local file
# 13. notify me that feedback has been sent and documented
# ----------

import nltk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    scrape()

def get_topic():
    cat_input = input('What is the category of the topic?')
    topic_input = input('Enter the topic you would like summarized.')
    return f'{cat_input} {topic_input}'



def scrape():
    driver = webdriver.Chrome()
    driver.get('https://en.wikipedia.org/wiki/Special:Search')
    elem = driver.find_element(By.NAME, 'search')
    # elem.clear()
    elem.send_keys(get_topic())
    elem.send_keys(Keys.RETURN)
    button = driver.find_element(By.CSS_SELECTOR,'.oo-ui-buttonElement > .oo-ui-inputWidget-input')
    button.click()



if __name__ == '__main__':
    main()
else:
    print('No')



