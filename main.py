from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)


classifier("how are you me")
# with open('text.txt','r') as f:
#     fi = f.readlines()
#     for fil in fi:
#         if fi == " ":
#             continue
#         print(classifier(fil))