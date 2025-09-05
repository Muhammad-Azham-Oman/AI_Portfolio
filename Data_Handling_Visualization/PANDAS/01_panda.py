import pandas

mydict = {
    "Value_a" : ["a","b","c","d"],
    "Value_b" : ["1","2","3","4"]
}

a = pandas.DataFrame(mydict)
print(a)