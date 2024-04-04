# 1 შექმენით ფუნქცია, რომელშიც გააერთიანებთ იმ ფუნქციებს რაც დღეს ვისწავლეთ (lower(), upper(), capitalize(), find())

def dav1():
  word1 = "NET"
  word2 = "goa"
  word3 = "bye"

  word1 = word1.lower()
  word2 = word2.upper()
  word3 = word3.capitalize()
  index = word2.find("G")

  

  return [word1, word2, word3, index]

print(dav1())

# 2 შექმენით ფუნქცია რომელსაც გადაეცემა list = ["name1" , "name2" , "name3"....] შემდეგ მომხმარებელს კითხეთ რომელი ინდექსის შეცვლა სურს და ამის მიხედვით შეცვალეთ ის კონკრეტული ინდექსი თქვენი სასურველი სტრინგით და ბოლოს შეაერთეთ join() ფუნქციის მეშვეობით 


def user_changeable_list(liist):
  print(f"This is the provided list: {liist}")
  asking = int(input("Which one of these words do you wish to change? (Choose from 0-5): "))
  removing = liist.pop(asking)
  adding = liist.insert(asking, "Ironman")
  combined = " ".join(liist)
  return liist

liist = ["I", "Love", "Fun", "Eating", "Movies", "Roses"]
print(user_changeable_list(liist))


# split() ფუნქცია გამოიყენება სტრინგის გასაყოფად ქვესტრინგებად რომლებიც თავსდება სიაში. სტრინგი იყოფა მითითებული character-ის დაყრდნობით.

# join() ფუნქცია გამოიყენება გარკვეული მიმდევრობის, მაგალითად list-ის ერთ გაერთიანებულ სტრინგად გადასაქცევად. 
# ის აცალკევებს სიაში ყველა ელემენტს რაღაც გარკვეული/მითითებული character-ით სანამ ერთ სტრინგად გადააქცევს.
 