# from fastapi import FastAPI
# import torch
# from pydantic import BaseModel
# from transformers import VitsModel, AutoTokenizer, set_seed
# #import numpy as np

# class Item(BaseModel):
#     text: str

# app = FastAPI()

# model = VitsModel.from_pretrained("facebook/mms-tts-eng")
# tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

# #torch.manual_seed(42)
# #np.random.seed(42)

# text = 'It cost me 125 dollars and it really sucks!.'


# @app.get("/")
# async def root():
#     return {"message": "Runny nose and runny yolk Even if u have a cold still"}

# #@app.get("/predict/")
# #async def predict():    
#     #with torch.no_grad():
#        # output = model(**inputs).waveform.float().numpy().tolist()
#    # return {"music": [output]}

# @app.post("/predict/")
# async def predict(item: Item):
#     inputs = tokenizer(item.text, return_tensors="pt")
#     with torch.no_grad():
#         out = model(inputs["input_ids"])
#         #attentions = out.attentions.float().numpy().tolist()
#         #hidden = out.hidden_states.float().numpy().tolist()
#         #spectrogram = out.spectrogram.tolist()
#         shape = out.waveform.shape 
#         lengths = out.sequence_lengths.numpy().tolist()
#         #output = out.waveform.float().numpy().tolist()
#     return {#"attentions":attentions,
#             #"hidden":hidden,
#             "shape": shape,
#             "lengths":lengths,
#             #"spectrogram":spectrogram,
#             #"music": output,
#             }
