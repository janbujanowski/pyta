from googlesearch import search
from bs4 import BeautifulSoup
import requests



def danceBitch():
    f = open("test.html", "w")
    myheaders = {
    'Cookie':'csrftoken=CCBbiUVwoFOQX7xZHiUXrWN8ZxnpDm6YabZCfeV2vyQuQQw3fTJ2q3CG0SC6BZli; _gcl_au=1.1.521459019.1691573143; _fbp=fb.1.1691573143447.721937824; sessionid=ojy9i2hoxwxiy8td2zehq3evdarkrybj; _gid=GA1.2.2104958349.1692785293; _gat_gtag_UA_119892649_1=1; _ga_2Y1TJKMJTN=GS1.1.1692796043.5.1.1692800557.0.0.0; _ga=GA1.1.2068471238.1691573143',
    'User-Agent': 'Mozilla/5.0'
    }
    pageObject = requests.get("https://www.examtopics.com/discussions/microsoft/view/69592-exam-ai-900-topic-1-question-120-discussion/")
    soup = BeautifulSoup(pageObject.text, features="html.parser")
    f.write(soup.prettify())
    f.close()

def setupVars():
    cssClassQuestionContent = 'card-text'
    cssClassQuestionAnswers = 'question-choices-container'
    cssClassQuestionSuggestedCorrectAnswer = 'correct-answer'
    cssClassQuestionCommentContent = 'comment-body/comment-content'
    cssClassQuestionCommentUpvoteCount = 'comment-body/comment-control/upvote-count'

def runScrapper():
    for number in range(5,6):
        searchphrase = f'examtopics ai-900 topic 1 question {number} discussion'
        print(f'searching for : {searchphrase}')
        results = search(f"{searchphrase}", advanced=True, sleep_interval=10, num_results=1)
        desiredurl = next(results).url
        print(f'{desiredurl}')
        pageObject = requests.get(desiredurl)
        soup = BeautifulSoup(pageObject.text, features="html.parser")
        #card = soup.find('p', class_"card-text')
        print(soup)
        # for each in card:
            # print(each)
        #print(bsPageContent.div)
        # bsPageContent.find("p", {"class": f"{cssClassQuestionContent}"})
        # for eachresult in results:
        #     print(eachresult.url)
    
danceBitch()