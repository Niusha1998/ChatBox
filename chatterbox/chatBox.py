print("niusha Teymoury")
import re
import long_responses as long



def massage_probability(user_massage,recognised_words,single_response=False,required_words=[]):
    massage_certainty=0
    has_required_words=True

    for word in user_massage:
        if word in recognised_words:
            massage_certainty +=1
            #recognise word probly is gone massage sorts by user and depended on how many words are written here
            percentage=float(massage_certainty)/float(len(recognised_words))

    for word in required_words:
        if word not in user_massage:
            has_required_words=False
            break

        if has_required_words or single_response:
            return int(percentage*100)
        
        else:
            return 0
        
def check_all_masseges(massage):
    hegiest_prop_list={}

    def response(bot_response,list_of_words,single_response,required_words=[]):
        nonlocal hegiest_prop_list
        hegiest_prop_list[bot_response]=massage_probability(massage,list_of_words ,single_response,required_words)


#responses by bot------------------------------------------------------------------------------------------------------------

    response("hello",["hi","salam","aniyong"],single_response=True)
    response("i am doing fine , and you?",["how", "are", "you", "doing"],required_words=["how"])
    response("thank you", ["i", "love", "code", "palace"] ,required_words=["code", "palace"])

    response(long.R_EATING, ["what", "you", "eat"], required_words=["you", "eat"])
    
    best_match=max(hegiest_prop_list , key=hegiest_prop_list.get())
   # print(hegiest_prop_list)
    
    print(best_match)

    return long.unknown()  if hegiest_prop_list[best_match] <1 else best_match






def get_response(user_input):
    #the bellow code only remove all cylabes from the massages and make just the clean words so it much recognize

    split_massage=re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response=check_all_masseges(split_massage)
    return response
#testing the response system
while True:
    print("bot: " + get_response(input("you: ")))
