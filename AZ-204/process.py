import os
import uuid
from bs4 import BeautifulSoup


cssClassQuestionContent = 'card-text'
cssClassQuestionAnswers = 'question-choices-container'
cssClassQuestionSuggestedCorrectAnswer = 'correct-answer'
cssClassQuestionCommentContent = 'comment-body/comment-content'
cssClassQuestionCommentUpvoteCount = 'comment-body/comment-control/upvote-count'

def process_file(filepath):
    html_to_output = [filepath, "</br>"]
    file = open(filepath,"r", encoding="utf-8")
    file_content = file.read()
    soup = BeautifulSoup(file_content, features="html.parser")
    cardtext = soup.find_all('p',{"class": cssClassQuestionContent})
    cardtext = str(cardtext).replace('src="/assets/media/exam-media','src="https://www.examtopics.com/assets/media/exam-media')+ "<br/>"
    html_to_output.append(cardtext)
    
    multiChoice = soup.find_all('div',{"class": cssClassQuestionAnswers})
    
    if(multiChoice):
        html_to_output.append(str(multiChoice))

    correct_answer = soup.find_all('span',{"class": cssClassQuestionSuggestedCorrectAnswer})
    correct_answer_guid = str(uuid.uuid4())
    correct_answer_div = "<button onclick=\"toggleHide(\'"+correct_answer_guid+"\')\">Toggle suggested answer</button><div id=\""+correct_answer_guid+"\" style=\"display: none;\" >"
    html_to_output.append(correct_answer_div)
    html_to_output.append("<b>Suggested Answer: </b>" + str(correct_answer).replace('src="/assets/media/exam-media','src="https://www.examtopics.com/assets/media/exam-media'))
    html_to_output.append("</div>")
    
    comment_section_guid = str(uuid.uuid4())
    comment_section_div = "<button onclick=\"toggleHide(\'"+comment_section_guid+"\')\">Toggle comments</button></br><div id=\""+comment_section_guid+"\" style=\"display: none;\" >"
    html_to_output.append(comment_section_div)
    comments_content = soup.find_all('div',{"class": "comment-body"})
    html_to_output.append(str(comments_content))
    html_to_output.append("</div>")
    return " ".join(html_to_output)

#         #card = soup.find('p', class_"card-text')

#         # for each in card:
#             # print(each)
#         #print(bsPageContent.div)
#         # bsPageContent.find("p", {"class": f"{cssClassQuestionContent}"})
#         # for eachresult in results:
#         #     print(eachresult.url)

html_output_contents = []
html_output_contents.append("<html>")
html_output_contents.append("<script async src=\"pytahelpers.js\"></script>")

folder_name = "AZ-204/rawhtml"
files = os.listdir(folder_name)
files.sort()
for filename in files:
    html_output_contents.append(process_file(folder_name + "/" + filename))

with open('AZ-204/final.html','w') as htmloutputfile:
    htmloutputfile.write(" ".join(html_output_contents))