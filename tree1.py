treeheight=input("Give tree height: ")
trunkheight=input("Give trunk height: ")
trunkwidth=input("Give trunk width: ")

i = 0

while i < treeheight:
 print((" " * (treeheight - i)) + ("*" * (i * 2 + 1)))
 i = i + 1
w=0


while w< trunkheight:
	print((" " * (treeheight)) + ("*" * trunkwidth ))
	w= w + 1
