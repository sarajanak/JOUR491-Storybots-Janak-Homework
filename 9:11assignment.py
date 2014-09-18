noun = ["Sara", "Amy", "Joe Biden", "Beyonce", "Ru Paul", "Walter White", "Gaga", "Matt", "Heidemann", "Blue Ivy"];
verb = ["fell asleep in class", "stole", "cursed", "pissed off fox news", "slayed", "cooked", "shaded your fave", "carried a drone accross campus", "acted like a shithead", "stole North West's baby Chanel handbag"];

print  choice.random, “%s was naughty, they %s today." % (noun, verb)




noun = ["Sara", "Amy", "Joe Biden", "Beyonce", "Ru Paul", "Walter White", "Gaga", "Matt", "Heidemann", "Blue Ivy"];
verb = ["fell asleep in class", "stole", "cursed", "pissed off fox news", "slayed", "cooked", "shaded your fave", "carried a drone accross campus", "acted like a shithead", "stole North West's baby Chanel handbag"];

>>>>for noun in verb:
...     print random.choice(noun), "was naughty. They", random.choice(verb), "today."
