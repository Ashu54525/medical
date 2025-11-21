import google.generativeai as genai

genai.configure(api_key='AIzaSyDfZllq-J4X6zpsrPtGNdeRVM8S0SSHfn4')

models = genai.list_models()

print("\nAvailable Models:\n")
for m in models:
    name = getattr(m, "name", None) or getattr(m, "model_id", None) or str(m)
    print(name)
