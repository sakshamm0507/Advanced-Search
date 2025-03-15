import os
import google.generativeai as genai

inp = input("Enter search query: ")
num = int(input("Enter number of queries to be generated: "))

# Configure Google Generative AI with your API key
API_KEY = " "  
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-pro-exp-02-05",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
a=" "
response = chat_session.send_message(f"convert the given query {inp} into {num} advanced search queries optimized for Google.   . Also give the site url and snnipet with for that site."
                                     f"Only return the queries nothing else enclosed in {a} and each query after a new line.")

response_arr = response.text.splitlines()

final_arr = []

for i in range (1,len(response_arr),2):
    final_arr.append(response_arr[i])
    print(response_arr[i])

print(final_arr)
