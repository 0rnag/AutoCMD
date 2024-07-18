from openai import OpenAI
import sys


prompt = input("Enter a prompt: ")
#for i in range(1, len(sys.argv)):
#    print(sys.argv[i])


'''
with open('.secrets.json') as f:
    secrets = json.load(f)
    API_KEY = secrets['SECRET_KEY_AUTOCMD']
'''

client = OpenAI()

def query_python(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful system administrator. You are helping a user by fulfilling their request. You only respond in clear python code. The code must be able to be ran by the interpreter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message

def query_shell(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Given a description of a task, generate a bash script that accomplishes this task. The response should be strictly the contents of the bash script, suitable for direct execution in a Unix/Linux environment, without any additional explanations, comments, or output. Please ensure the script is complete, syntactically correct, and secure for execution."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message



result = query_shell(prompt).content

print(result)

with open('output.sh', 'w') as f:
    f.write(result)
