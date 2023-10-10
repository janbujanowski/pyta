import os
from bs4 import BeautifulSoup


cssClassQuestionContent = 'card-text'
cssClassQuestionAnswers = 'question-choices-container'
cssClassQuestionSuggestedCorrectAnswer = 'correct-answer'
cssClassQuestionCommentContent = 'comment-body/comment-content'
cssClassQuestionCommentUpvoteCount = 'comment-body/comment-control/upvote-count'

def process_file(filepath):
    file = open(filepath,"r", encoding="utf-8")
    file_content = file.read()
    soup = BeautifulSoup(file_content, features="html.parser")
    cardtext = soup.find_all('p',{"class": cssClassQuestionContent})
    print(cardtext)                 

#         #card = soup.find('p', class_"card-text')

#         # for each in card:
#             # print(each)
#         #print(bsPageContent.div)
#         # bsPageContent.find("p", {"class": f"{cssClassQuestionContent}"})
#         # for eachresult in results:
#         #     print(eachresult.url)


folder_name = "AI-900/rawhtml"
files = os.listdir(folder_name)
files.sort()
for filename in files:
    process_file(folder_name + "/" + filename)