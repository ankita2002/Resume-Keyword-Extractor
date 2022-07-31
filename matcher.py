import textract
import os
import re

# returns keywords that matched in content
# @param content: String containing content of file
# @param keywords: List of keyword
def matcher(content, keywords):
  keywordsFound = []
  for keyword in keywords:
    if (re.search(re.escape(keyword.lower()), content)):
      keywordsFound.append(keyword)
  return keywordsFound

# driver test code
# content = "I love html css. I create nice websites that work on desktops, mobiles and literally any device with a browser and a screen."
# keywords = ["html", "", "python"]
# print(matcher(content, keywords))