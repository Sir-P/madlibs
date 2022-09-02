"""This game accepts word imports from users and generates a story from those word inputs"""
word1 = input('Enter a noun: ')
word2 = input('Enter a plural noun: ')
word3 = input('Enter a verb(present tense): ')
word4 = input('Enter a verb(present tense): ')
word5 = input('Enter part of body(plural): ')
word6 = input('Enter an adjective: ')
word7 = input('Enter a plural noun: ')
word8 = input('Enter an adjective: ')

story = f"Today, every students has a computer small enough to fit into his/her {word1}. He/She can solve any math problem by simply pushing the computer's little {word2}. Computers can add, multipky, divide and {word3}. They can also {word4} better than a human. Some computers are {word5}. Others have a/an {word6} screen that shows all kinds of {word7} and {word8} figures"
print(story)