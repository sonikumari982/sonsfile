import random


words=["manu","soni","apple","shlini","pagal","bedtime","memorie",
"trend","enjoyed","qualitt","hearing","stories"]
choos=random.choice(words)
# print(choos)
print(" -------\n",
      "|     |\n",
      "|\n",
      "|\n",
      "|\n",
      "|\n",
      "---------")
lenofwords=len(choos)
#print(lenofwords)
strword=""
pozition=1
c=0
i=0
while i<len(choos):
    pozition+=1
    guess=input("guess the latter of words\n")
    if guess == choos[i]and i==i:
        strword+=guess
        print("your correct give",pozition ,"word")
    elif guess !=choos[0]and c==0:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|\n",
              "|\n",
              "|\n",
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess !=choos[1]and c==1:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|     |\n",
              "|\n",
              "|\n",
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess!=choos[2]and c==2:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|    /|\n",
              "|\n",
              "|\n",
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess!=choos[3] and c==3:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|    /|\ ","\n",
              "|\n",
              "|\n"
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess!=choos[4] and c==4:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|    /|\ ","\n",
              "|     |\n",
              "|\n",
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess!=choos[5] and c==5:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|    /|\ ","\n",
              "|     |\n",
              "|    /\n",
              "---------")
        print("wrong guess give",pozition,"word")
    elif guess!=choos[6] and c==6:
        strword+=guess
        c=c+1
        print(" -------\n",
              "|     |\n",
              "|     0\n",
              "|    /|\ ","\n",
              "|     |\n",
              "|    / \ ","\n"
              "---------")
        print("wrong guess give",pozition,"word")
    if strword!=choos and i==len(choos)-1:
        # print(" -------\n",
        #       "|     |\n",
        #       "|     0\n",
        #       "|    /|\ ","\n",
        #       "|     |\n",
        #       "|    / \ ","\n"
        #       "---------")
        print("'ooh no' so sad your words not correct")
        print("game finish")
    if strword==choos:
        print("you are winner")
        print("game finish")
    i=i+1