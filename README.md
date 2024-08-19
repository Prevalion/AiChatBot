# AiChatBot
My first project that involves interaction with AI using Using [Nvidia NIM API](https://build.nvidia.com/explore/discover), that gives access to more some good AI language model.
## Steps:
1. Clone, download or even use codespace.
2. Install the requirements.txt by typing: pip install -r requirements.txt, it will do the job for you.
3. Go to [Nvidia NIM API](https://build.nvidia.com/explore/discover), make an account, choose a model, get your API key, and put then in corresponding place
### Some notes:
When the user hit send, the app will frozen for a moment, this is because it is waiting for a respond from the api, and the duration depends on how long the message is.
The API is valid for one day, so you have to generate a new key every day (i know it's inconvenient).