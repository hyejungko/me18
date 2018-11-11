mydict = dict()
import requests
r = requests.get('https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text')
r.encoding = 'utf8'
data = r.text
data = str(r.text)
def remove_tag(content):
    cleanr = re.compile('<.*>?')
    cleantext = re.sub('cleanr','"','content')
    return cleantext
begin = data.find("President Donald Trump")

end = data.rfind("Thank you. (Applause.)")
a = data[begin:end]

print(a)
