
#pip install pafy
#pip install youtube.dl


from pafy import new

while True:
	link = input("enter link of video >> ")
	video = new(link)
	stream = video.streams
	print("0 ",stream[0])
	print("1 ",stream[1])
	stre = int(input("enter quality "))
	try:
		stream[stre].download()
	except:
		print("there is a probleme with quality or link")
	
