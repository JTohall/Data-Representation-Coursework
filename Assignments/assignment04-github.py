# Data Representation - Assignment 4
# Author: Jamie Tohall

# Write a program in python that will read a file from a repository. The program should then replace
# all the instances of the text "Andrew" with your name. The program should then commit those 
# changes and push the file back to the repository.

# Import relevant modules
import requests
from github import Github
from config import config as cfg 

# read in API key
apikey = cfg["githubkey"] # Key
g = Github(apikey)

repo = g.get_repo("yourccount/yourrepo")
# print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text

# Replace Andrew with Jamie
newContent = contentsofFile.replace('Andrew', 'Jamie')
#print (contentOfFile)
print (newContent)


# Push file back to repository
gitHubResponse = repo.update_file(fileInfo.path,"replace A with J",newContents,fileInfo.sha)

print (gitHubResponse)


