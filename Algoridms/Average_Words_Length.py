
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def Avarage():
    sentence1 = "Hi all, my name is Tom...I am originally from Australia. I lived in Canberra"
    sentence2 = "I need to work very hard to learn more about algorithms in Python!"

    sentence1_list = list(sentence1)
    sentence2_list = list(sentence2)

    #counting
    sentence1_lenth = list.__len__(sentence1_list)
    sentence2_lenth = list.__len__(sentence2_list)

    if sentence1_lenth >= sentence2_lenth:
        print("Sentence1 is higher !")
        counting1 = int(sentence1_lenth) / int(sentence2_lenth)
        print(counting1)

    else:
        print("Sentence2 is Higher !")
        counting2 = int(sentence2_lenth) / int(sentence1_lenth)
        print(counting2)

print(Avarage())
