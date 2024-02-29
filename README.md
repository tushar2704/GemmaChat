# GemmaChat
Smart Chat using Gemma model via Ollama, LangChain and Chainlit

Coming up:Deployment, more feature and custom UI


## Steps to Replicate 

1. Fork this repository and create a codespace in GitHub as I showed you in the youtube video OR Clone it locally.
   ```
   git clone https://github.com/tushar2704/GemmaChat.git
   cd GemmaChat
   ```

2. Create a virtualenv and activate it
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

3. OPTIONAL - Rename example.env to .env with `cp example.env .env`and input the environment variables from [LangSmith](https://smith.langchain.com/). You need to create an account in LangSmith website if you haven't already.
   ``` 
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY="your-api-key"
   LANGCHAIN_PROJECT="your-project"
   ```

4. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run main.py
   ```


