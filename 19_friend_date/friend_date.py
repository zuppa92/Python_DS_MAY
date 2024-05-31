def friend_date(a, b):
    elmo = ('Elmo', 5, ['hugging', 'being nice'])
    sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
    gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

    friend_date(elmo, sauron)
    False

    friend_date(sauron, gandalf)
    True

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))  # Output: False
print(friend_date(sauron, gandalf))  # Output: True
