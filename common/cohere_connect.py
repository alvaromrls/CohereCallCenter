import json
import cohere
import requests

f = open("config.json")
config = json.load(f)

key = config["cohereKey"]

print(key)
text = "The string to be tokenized, the minimum text length is 1 character, and the maximum text length is 65536 characters."

co = cohere.Client(key)

response = co.tokenize(
    text=text,
)

print(response)
