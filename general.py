import os
import openai
# import gradio
from dotenv import load_dotenv

load_dotenv()

api = os.environ.get('OPENAI_API_KEY')

openai.api_key = os.environ.get('OPENAI_API_KEY')

system_contents = [
    'Be FUN! Use lots of JOKES!',
    'Your name is Chatty',
    'Use emoticons and lots and lots of relevant EMOJIS everywhere, be friendly.',
    'Show enthusiasm and positivity: Use exclamation' + 
    'marks and positive language to show enthusiasm and positivity in your answers.',
    'Use friendly greetings and closings.',
    'Try to be as helpful as possible.',
    'If relevant give examples and especially categorise the examples.', 
    'Such as if asked about clothing, give example about the types of clothing but do not explain them long, give the names in short.', 
    'This examples should be just names shortly.', 
    'Do not explain as long as not wanted.'
    'Use their name: Address the person by their name in your answers.',
    'Use kind and supportive language: Be mindful of your choice of words' +
    'and use language that is kind, supportive, and encouraging. Avoid using' + 
    'harsh or critical language that may be misinterpreted in your answers.',
    "Show interest and ask questions: Demonstrate genuine interest in the other" + 
    "person's life or experiences by asking questions and actively engaging in the" + 
    "conversation. This shows that you care about them and their well-being."
    "Use compliments and affirmations: Compliment the other person or express" + 
    "appreciation for something they shared. It helps create a positive and friendly" +
    "atmosphere.",
    'Keep answers short and try to be concise.',
    'At the end of yoru reply always say whether the question is about shopping or not!'
]

user = {
    'name': 'Fredo',
    'age': 22,
    'married': False,
    'sex': 'male',
    'has_crush': True,
    'profession': 'Developer. Solidity developer.'
}

pronouns = ['He' if user['sex'] == 'male' else 'She' ,'His' if user['sex'] == 'male' else 'Her']

user_info = [
    f"Here is data about current user: {pronouns[1]} name is {user['name']},",
    f"{pronouns[0]} is {user['age']} years old,",
    f"{pronouns[0]} is {'' if user['married'] else 'not'} married,",
    f"{pronouns[0]} has {'' if user['has_crush'] else 'not'} crush,",
    f"{pronouns[0]} is {user['profession']}."
]

messages = [
    {'role': 'system', 'content': ''.join(system_contents)},
    {'role': 'system', 'content': ''.join(user_info)}
]

def chat(input):
    messages.append({'role': 'user', 'content': input})
    answer = openai.ChatCompletion.create(
        max_tokens=500,
        model="gpt-3.5-turbo",
        messages=messages)
    messages.append(
        {'role': 'assistant', 'content': answer.choices[0].message.content})
    return answer.choices[0].message.content



while True: 
    question = input('Enter: ')
    if not question:
        print('Have a good day! Nice to help you ✨')
        break
    print(chat(question))