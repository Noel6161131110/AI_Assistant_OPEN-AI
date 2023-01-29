import openai

#openai.api_key = os.getenv('API_KEY') #Setting GPT-3 API-KEY (text-davinci-002)

openai.api_key_path = 'apikey.txt'


def response_Summary(document_Text):   
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt = document_Text,
        temperature= 0.8,
        max_tokens= 1500,

    )
    return response["choices"][0]["text"]

    