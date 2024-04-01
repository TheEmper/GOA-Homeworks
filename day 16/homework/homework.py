# 1  გადაიმეორეთ ფუნქციები სოლოლეარნის გამოყენებით და გააკეთეთ თქვენი კრეატიულობით 5 ფუნქცია, 2 ფუნქცია რომელიც არ აბრუნებს მნიშვნელობას

def greeting():
    print("Hello! Welcome to the program.")

def vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for i in word:
        if i in vowels:
            vowel_count += 1
    print("Number of vowels:", vowel_count)

# 1.5 3 ფუნქცია რომელიც აბრუნებს მნიშვნელობას
    
def reverse_list(liiist):
    return liiist[::-1]

def calculate_average(liiist):
    return sum(liiist) / len(liiist)

def max(liiist):
    return max(liiist)


# 3 შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე, დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული 

def sum_of_odd_even(liiist):
    odd_list = []
    even_list = []
    for i in liiist:
        if i % 2 == 0:
            odd_list.append(i)
        else:
            even_list.append(i)
    
    sum_odd = sum(odd_list)
    sum_even = sum(even_list)
    return [sum_odd, sum_even]


# 4  შექმენით ფუნქცია რომელიც დაგიბრუნებთ სიაში მყოფ ელემენტების რაოდენობას

def elements_in_list(liiist):
    return len(liiist)



    

