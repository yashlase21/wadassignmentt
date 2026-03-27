import random
friend = ["Yash","Raj","Veer","Swayam","Shubham","Rahul"]
# Option1
print(random.choice(friend))
# Option2
random_index = random.randint(0,5)
print(friend[random_index])