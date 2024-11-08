import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])


# response =  client.chat.completions.create(model='gpt-3.5-turbo', messages=[{"role":"user", "content": "count 1 to 10"}])

# print(response.choices[0].message.content)


def generate_story(words):
    # Call OPENAI API to generate the story
    response = get_short_story(words)

    # format and return the response
    return format_response(response)



def get_short_story(words):
    
    system_prompt = f"Make 10 questions and answers based on this {words}"

    response = client.chat.completions.create(model='gpt-3.5-turbo',messages=[{"role":"user","content": system_prompt}], temperature=0.8, max_tokens=1500)

    return response

def format_response(response):

    story = response.choices[0].message.content
    story = story.strip()
    return story



