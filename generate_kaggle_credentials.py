import json, os

os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)

# note: you must replace YOUR_USERNAME and YOUR_API_KEY with your actual username and Kaggle API key
# see kaggle.com for details
kaggle_api_token = {"username": "YOUR_USERNAME", "key": "YOUR_API_KEY"}
with open(os.path.expanduser("~/.kaggle/kaggle.json"), 'w') as file:
    json.dump(kaggle_api_token, file)

os.chmod(os.path.expanduser("~/.kaggle/kaggle.json"), 600)
