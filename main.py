import requests
# import torch
# from transformers import BartForConditionalGeneration, BartTokenizer

# this method takes the AI generated text and returns the plagiarism percentage the less the score the better and more humanly the text looks
def plagiarism_check(text):
    url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"

    payload = {
        "text": text,
        "language": "en",
        "includeCitations": False,
        "scrapeSources": False
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ADD_YOUR_OWN_API_KEY",
        "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    return (response_json["percentPlagiarism"])

def paraphrase_v1(text):
    url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"

    payload = {
        "text": text,
        "result_type": "multiple"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ADD_YOUR_OWN_API_KEY",
        "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

# # this method takes the AI generated text and then paraphrases the text into a more humanly format
# def paraphrase_v2(text):
#     model = BartForConditionalGeneration.from_pretrained('eugenesiow/bart-paraphrase')
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     model = model.to(device)
#     tokenizer = BartTokenizer.from_pretrained('eugenesiow/bart-paraphrase')
#     batch = tokenizer(text, return_tensors='pt')
#     generated_ids = model.generate(batch['input_ids'])
#     generated_sentence = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

#     return (generated_sentence)[0]

# this method takes the topic for the essay as input along with the word limit and returns the AI generated essay

def essay_generator(topic, word_count):
    url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
            "content": "you are good in english language and now you will write an essay on the topic : " + topic + " in " + word_count + " words and make sure there a little bit grammatical mistakes in between just a little bit" 
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ADD_YOUR_OWN_API_KEY",
        "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    return (response_json["choices"][0]["message"]["content"])

essay_topic = input("Enter the topic of your essay : ")
word_count = input("Enter the word count of your essay : ")
print("Generating your essay...")
content = essay_generator(essay_topic, word_count) # generating essay with AI
confidence_score = plagiarism_check(content) # plagiarism checker generates a confidence score the less the score the better
rephrased_content_list = paraphrase_v1(content) # array of paraphrased content with 4 items
i = 0

print("Paraphrased content : \n")

while confidence_score != 0 or i == 4:
    # content = essay_generator(essay_topic, word_count, "Please paraphrase this entire essay without changing the meaning")
    content = rephrased_content_list[i]
    confidence_score = plagiarism_check(rephrased_content_list[i])
    i = i + 1

print(content)
