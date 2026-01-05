import os
from tkinter import Tk, Entry, Text, Button, END, WORD
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

root = Tk()

def send():
    user_input = msg.get()
    client = OpenAI(
        base_url="https://api.tokenfactory.nebius.com/v1/",
        api_key=os.getenv("NEBIUS_API_KEY")
    )
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True,
    )
    text.insert(END, "\nYou: " + user_input + "\n", "user_tag")
    bot_response = ""
    for chunk in completion:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content is not None:
            bot_response += delta.content
    text.insert(END, "Bot: " + bot_response, "bot_tag")
    msg.delete(0, END)


# window config
# configure grid row/column weights for responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# create a Text widget with scrollbars
text = Text(root, bg="#012456", fg="white", wrap=WORD)
text.grid(row=0, column=0, columnspan=2, sticky="nsew")
# create entry and button widgets
msg = Entry(root, width=80)
msg.grid(row=1, column=0, sticky="ew")
text.tag_config("user_tag", foreground="white", font=("Helvetica", 10, "bold"))
text.tag_config("bot_tag", foreground="yellow", font=("Helvetica", 10, "bold"))
send_button = Button(root, text="Send", bg="black", fg="white", width=20, command=send)
send_button.grid(row=1, column=1, sticky="ew")
# bind the enter key to the send function
msg.bind("<Return>", lambda event: send())
root.title("Chat with LLaMa")
root.mainloop()
