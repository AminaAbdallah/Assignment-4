import json
import pandas
import requests
#MyApiKey : 'b7de039e294740bb84d8dff8c2bbf97d'
# The headers for the authentification

print('NB : the result of this request will be found in the console or in the csv file that you choose its location in the code in the end')

print('Please, enter your Apikey for APInews or you can use mine in the comment up')
headers = {'Authorization':input()}

# The addpoint that I need to have Top headlines
top_headlines_url = 'https://newsapi.org/v2/top-headlines'

#The question is for the user
print('From which country do you want to have headlines news ? ')

#the request parameter is the country, it will be an input
headlines_payload = {'country':input()}



#we will use get from the module requests
response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload )
print(response)
# Priny the response in json file
pretty_json_output = json.dumps(response.json(), indent=4)
#print(pretty_json_output)

# Convert response to a json string
response_json_string = json.dumps(response.json())

print(response_json_string)
# retrieve json objects to a python dict
response_dict = json.loads(response_json_string)

# Info about articles is represented as an array in the json response
# A json array is equivalent to a list in python

articles_list = response_dict['articles']

# sources_list = response_dict['sources'] if we want info only about sources

# Convert articles list to json string , convert json string to dataframe , write df to csv!
df = pandas.read_json(json.dumps(articles_list))

# Using Pandas write the json data to a csv
#You can edit the emplacement of the csv file here
df.to_csv(r'C:\Users\octet plus\Desktop\Headlines .csv')
