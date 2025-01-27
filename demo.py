# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="./llama-2-7b-chat.ggmlv3.q8_0.bin", verbose=True, n_ctx=4096)
print('model loaded')
# create a text prompt
text="Hello What is your name sir please tell me full name please.ok,My name is suvarna Dnyandev Pawar.then tell me what is your location.i am belong from pune maharashtra.ok.then tell me what is your occupation sir/madam.i am software engineer.then what is your yearly income in lakhs.my income is 5 lakh.tell me your mother name.my mother name is usha pawar.what is your birth of date?My birth of date is 29 may 2000."
prompt = "This is a conversation between a customer and Agent for KYC Process. Extract the following information from the conversation and provide it in valid JSON format: customer Full Name, Location,Occupation,Income,Mother Name,Date of birth. \
          Conversation: {text} \
          Details to include: customer Full Name, Location,Occupation,Income,Mother Name,Date of birth. \
          Answer: "


        
# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
