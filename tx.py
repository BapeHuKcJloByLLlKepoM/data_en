# from transformers import VitsModel, AutoTokenizer
# import torch

# model = VitsModel.from_pretrained("facebook/mms-tts-eng")
# tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

# text = "welcome to the cum zone"

# inputs = tokenizer(text, return_tensors="pt")

# with torch.no_grad():
#     output = model(**inputs).waveform[0]

# #сохранение  wav

# import scipy

# <put.float().numpy())

# # отображение аудио сразу 

# from IPython.display import Audio

# Audio(output.numpy(), rate=model.config.sampling_rate)
