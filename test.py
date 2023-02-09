import re 
page = 'https://www.youtube.com/@PaniBottle/videos'
userName = re.findall('@([a-zA-Z0-9]+)', page)
Download = input('Enter')
DOWN_DIRT = Download+'\\' + str(userName[0])
print(DOWN_DIRT)