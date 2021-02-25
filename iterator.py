import json

class Country:

    def __init__(self, file_default, file_end):
        self.file_default = file_default
        self.file_end = file_end

    def download(self):
        country_dict = dict()
        with open(self.file_default, encoding='ascii') as f:
            data = iter(json.load(f))
            for i in data:
                if ' ' in i['name']['common']:
                    country_dict[i['name']['common']] = 'https://en.wikipedia.org/wiki/' + str(i['name']['common'].replace(" ", "_"))
                else:
                    country_dict[i['name']['common']] = 'https://en.wikipedia.org/wiki/' + str(i['name']['common'])
        with open(self.file_end, 'w') as f:
            json.dump(country_dict, f, indent=2)



mycountry = Country('countries.json', 'country.json')
mycountry.download()



