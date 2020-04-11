def replace(sentence):
    newSentence = []
    for word in sentence:
        if (word == 'ADJECTIVE' or word == 'ADJECTIVE.'):
            newSentence.append(input('Nhap mot ADJECTIVE vao: \n'))
        elif (word == 'ADVERB' or word == 'ADVERB.') :
            newSentence.append(input('Nhap mot ADVERB vao: \n'))       
        elif (word == 'NOUN' or word == 'NOUN.'):
            newSentence.append(input('Nhap mot NOUN vao : \n'))
        elif (word == 'VERB' or word == 'VERB.'):
            newSentence.append(input('Nhap mot VERB vao: \n'))
        else:
            newSentence.append(word)
    return newSentence

sentenceFile = open('sentenceStructure.txt' , 'r')
sentence =  (sentenceFile.read()).split(' ')

sentence = replace(sentence)
print(' '.join(sentence))

new = open('reconstructedSentense.txt', 'w')
new.write(' '.join(sentence))

new.close()
sentenceFile.close()



        