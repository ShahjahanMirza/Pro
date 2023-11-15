import requests
request = requests.get("https://raw.githubusercontent.com/ShahjahanMirza/100-Machine-Learning-Projects/master/helper_function.py")
with open("helper_function.py", "wb") as f:
  f.write(request.content)


from helper_function import automted_file_creator

automted_file_creator('e:/Projects/')
