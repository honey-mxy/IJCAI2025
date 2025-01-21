import openai


def get_chat_messages(prompt_text):
    openai.api_key = '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'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=prompt_text,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message.content

# 定义对话信息
prompt_text = [{"role": "system", "content": "You are an expert in Python."},
                {"role": "user", "content": "Please tell me the basics of Python."},
                {"role": "assistant", "content": "1. Installation:...2. Hello, World!:...3. ..."}
                 ]

# 调用ChatGPT API生成回复
response_content = get_chat_messages(prompt_text)

# 打印生成的回复
print("ChatGPT回复：", response_content)

