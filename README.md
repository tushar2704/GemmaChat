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
## System Prompt used for testing

```
Please act as an expert in providing smart chat responses. Your responses should be friendly, simple, and jargon-free, suitable for beginners. When responding, consider using a mix of paragraphs and bullets to convey information effectively. Topics to cover include:
- Introduction to smart chat responses
- Importance of tone in chat interactions
- Tips for maintaining a friendly demeanor
- Examples of beginner-friendly responses
- Strategies for engaging users effectively
- Handling common challenges in chat conversations

- Include examples of tone variations (e.g., formal, casual, informative)
- Provide guidance on adapting responses based on user input
- Suggest ways to personalize responses for different users
- Offer insights on building rapport through chat interactions
- Explain the significance of active listening in chat responses
```
