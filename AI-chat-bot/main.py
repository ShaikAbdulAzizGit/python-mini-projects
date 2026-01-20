import requests
from secret_key import api_key


def get_chatbot_reply(user_input,key):
        url="https://openrouter.ai/api/v1/chat/completions"
        
        payload = { "model": "meta-llama/llama-3.3-70b-instruct:free",
                    "messages": [
                         {"role":"system","content": "You are a person named Shaik Abdul aziz you can speak hidi as well as english . You analyse the chat history and respond like Shaik abdul aziz based on the chat history"},
                        {"role": "user", "content": f"{user_input}"}
            ]
            }
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url, json=payload, headers=headers)

            data=response.json()

            chatBot_reply=data['choices'][0]['message']['content']

            return chatBot_reply
        except Exception as e:
            return "Sorry something went wrong please check your internet and try again"

def main():
     print("Hey I am chatbot How can I help you . click 'quit' or 'exit' to stop")
     key=api_key
     while True:
          user_input=input("You: ").strip()
          if not user_input:
               print("Try entering something")
               continue
          if user_input.lower() in ['exit','quit']:
               print("Goodbye !...")
               break
          else:
               reply=get_chatbot_reply(user_input,key)
               print(f"Chatbot:{reply}")

if __name__=="__main__":
    main()

