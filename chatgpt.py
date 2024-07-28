# pip install openai
import openai

def main():
    # Initialize the OpenAI client
    openai.api_key = ''

    # Create a chat completion
    completion = openai.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    # Print the response
    print(completion.choices[0].message.content)




if __name__ == "__main__":
    main()
