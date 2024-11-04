from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Set your API key here

# Make an API request using the new format
response = client.chat.completions.create(model="gpt-3.5-turbo",  # Use "gpt-4" if needed
messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "I like coffee more than tea, tea more than juice, and juice more than tea"},
  {"role": "user", "content": "What's my ranking?"}
])

# Print the response
print(response.choices[0].message.content.strip())

response_2 = client.chat.completions.create(model="gpt-3.5-turbo",  # Use "gpt-4" if needed
messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "I like coffee more than tea, juice more than tea, and tea more than juice"},
  {"role": "user", "content": "What's my ranking?"}
])

# Print the response
print(response_2.choices[0].message.content.strip())

response_3 = client.chat.completions.create(model="gpt-4-turbo",  # Use "gpt-4" if needed
messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "I like coffee more than tea"},
  {"role": "user", "content": "I like juice more than coffee"},
  {"role": "user", "content": "I like tea more than juice"},
  {"role": "user", "content": "What's my ranking?"}
])

# Print the response
print(response_3.choices[0].message.content.strip())
