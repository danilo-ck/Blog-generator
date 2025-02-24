from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(
    api_key=config["API_KEY"]
)

def generate_headers(topic):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Generate 3 interesting section headers for a blog post about {topic}. Return only the headers, one per line, numbered 1., 2., 3.",
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip().split('\n')

def generate_paragraph(header):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write a detailed paragraph for the following blog section header: {header}",
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].text.strip()

def generate_blog_content():
    topic = input('What main topic would you like to write about? ')
    print("\nGenerating headers...\n")
    
    headers = generate_headers(topic)
    complete_blog = []
    
    print("Generated headers:")
    for header in headers:
        print(header)
    
    print("\nGenerating paragraphs for each header...")
    for header in headers:
        complete_blog.append(f"\n{header}\n")
        complete_blog.append(generate_paragraph(header))
        print(f"\nCompleted section: {header}")
    
    print("\n=== COMPLETE BLOG ===\n")
    print('\n'.join(complete_blog))

while True:
    answer = input('\nGenerate a new blog? (Y for yes, anything else to quit): ')
    if answer.upper() != 'Y':
        break
    generate_blog_content()