import sys
import os
import openai
import requests
from bs4 import BeautifulSoup
import re
openai.api_key = os.getenv("OPENAI_API_KEY")

issue_url = 'https://github.com/Jonathan-Zollinger/eDirectory-Compose/issues/1'
pattern = r'(https://github.com/[^/]+/[^/]+)/.*'
match = re.search(pattern, issue_url)

if match:
    repository_url = match.group(1)
    print("Repository URL:", repository_url)
else:
    print("Invalid GitHub issue URL")
response = requests.get(issue_url)
soup = BeautifulSoup(response.content, 'lxml')
issue_description = soup.find(class_='markdown-body').get_text()
# Define the GitHub file URL
url = 'https://github.com/Jonathan-Zollinger/eDirectory-Compose/blob/main/src/eDir_utils.sh'
print(url)
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# Find all the code blocks in the file content
fileContents = ""
code_blocks = soup.find_all('div', class_='highlight')
for block in code_blocks:
    if block.find('span', {'class': 'nf'}) and block.find('span', {'class': 'kd'}) == 'def':
        fileContents += code_block.find('pre').text


# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Use the following instructions: " + issue_description + " to generate a README file in markdown given the following file: " + fileContents,
#   temperature=0.7,
#   max_tokens=979,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
#   )

print("Use the following instructions: " + issue_description + " to generate a README file in markdown given the following file: " + fileContents)
