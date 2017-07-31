#Second Round of Exercises

#Create a Guest List
invitations = ['emily', 'barack obama', 'jackie chan']
print("Hello, " + invitations[0].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[1].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[2].title() + "! You are cordially invited to my party.")

#Changing Guest List
print(invitations[1].title() + " couldn't make it. :(")
invitations[1] = 'bill gates'
print("Hello, " + invitations[0].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[1].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[2].title() + "! You are cordially invited to my party.")

#Add Three Guests
print("We found a bigger dining table.")
invitations.insert(0, 'jayme figueroa')
invitations.insert(2, 'abbie lin')
invitations.append('matt damon')
print("Hello, " + invitations[0].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[1].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[2].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[3].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[4].title() + "! You are cordially invited to my party.")
print("Hello, " + invitations[5].title() + "! You are cordially invited to my party.")

#3-7 Shrinking Guest List
print("Sorry, we can only invite two people.")
removed_invitee = invitations.pop(-1)
print("My bad, " + removed_invitee.title() + ".")
removed_invitee = invitations.pop(-1)
print("My bad, " + removed_invitee.title() + ".")
removed_invitee = invitations.pop(-1)
print("My bad, " + removed_invitee.title() + ".")
removed_invitee = invitations.pop(-1)
print("My bad, " + removed_invitee.title() + ".")

print("You're still invited, " + invitations[0].title() + "!")
print("You're still invited, " + invitations[1].title() + "!")

del invitations[0]
del invitations[0]

print(invitations)
