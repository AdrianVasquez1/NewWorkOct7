# There is a comparison in between ring that describes the number of people
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

print(w + e)

# more stuff 10/8

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why did it use %r instead of %s?
# We formatted the code with %r instead of %s

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# What if I didn't Jan being listed on the line with the rest of the
# text and away from the months? How could I fix that?\

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non time."
backslashCat = "I'm \\ a \\ cat."
taskCat =  """
I'll make a list:
\t*Cat Food
\t*Fishies
\t*Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(taskCat)

# Escape Seq what does it do?

# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uxxx
# \uxxxxxxxx
# \v
# \ooo
# \xhh

# What's the following code do:
# while True
#   for i in ["/", "-", "|", "\\", "|"]:
#       print("%s\r" % i, end='')

# Can you replace """ with '''?