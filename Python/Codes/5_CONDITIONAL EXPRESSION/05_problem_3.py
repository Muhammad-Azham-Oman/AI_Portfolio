c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

a = input("Enter your comment: ")

if((c1 in a)or(c2 in a)or(c3 in a)or(c4 in a)):
    print("This comment is a spam")

else:
    print("Thanks for your comment")