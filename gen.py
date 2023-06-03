import sys
import os
import openai
import requests
import bs4
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Use the following instructions: " + issue_description + " to generate a README file in markdown given the following repository: " + repository
  temperature=0.7,
  max_tokens=979,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

issue_url = 'https://github.com/Jonathan-Zollinger/eDirectory-Compose/issues/1'
response = requests.get(issue_url)
soup = bs4(response.content, 'lxml')
issue_description = soup.find(class_='markdown-body').get_text()


print(issue_description)
