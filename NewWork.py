# There is a comparison in between a string that describes the number of people
x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s." % (binary, doNot)

print(x)
print(y)

#  There is a string within a string creating one sentence
print("I dsof: %r" % x)
print("I also said: '%s'." % y)

# A string evaluation is taking place comparing the joke to whether or not it is funny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

# There is two string creating one whole line when they are added together
w = "This is the left side of ..."
e = "a string with a right side"

print( w + e)