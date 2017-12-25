word=input("Enter few words using comma: ")

separate= word.split(',')

separate.sort()

final_words=",".join(separate)

print(final_words)




