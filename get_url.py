import webbrowser
import pyperclip

# Get a list of all open tabs
tab_list = webbrowser.get().tabbed_browser.tabs

# Loop through the tabs and copy the URL to the clipboard
urls = []
for tab in tab_list:
    urls.append(tab.browser.url)
    pyperclip.copy('\n'.join(urls))

# Print the list of URLs
print(urls)