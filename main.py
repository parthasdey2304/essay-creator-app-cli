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
        "X-RapidAPI-Key": "ADD_YOUR_API_KEY_HERE",
        "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    return (response_json["percentPlagiarism"])

# def paraphrase_v1(text):
#     url = "https://paraphrasing-api2.p.rapidapi.com/long-rewriter"

#     querystring = {
#         "text":text,
#         "unique":"1",
#         "mode":"fluent"
#         }

#     headers = {
#         "X-RapidAPI-Key": "c6150aa0fbmshc0a1461851bd7ecp100c48jsnac068272b7e6",
#         "X-RapidAPI-Host": "paraphrasing-api2.p.rapidapi.com"
#     }

#     response = requests.post(url, headers=headers, params=querystring)

#     return (response.json())

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
def essay_generator(topic, word_count, prefix = "you are an expert in english language and now you will write an essay on the topic : "):
    url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
            "content": prefix + " " + topic + " in " + word_count + " words"
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ADD_YOUR_API_KEY",
        "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    return (response_json["choices"][0]["message"]["content"])

essay_topic = input("Enter the topic of your essay : ")
word_count = input("Enter the word count of your essay : ")
content = essay_generator(essay_topic, word_count)
confidence_score = plagiarism_check(content)

while confidence_score != 0:
    content = essay_generator(essay_topic, word_count, "Please paraphrase this entire essay without changing the meaning")
    confidence_score = plagiarism_check(content)

print(content)
