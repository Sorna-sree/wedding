lunch=int(input("enter the cost of the lunch"))  #cost for the lumch per person
breakfast=lunch//2    #per person is half of the lunch
hall=lunch//3    #one third of the per person
decorations=hall//2 #50% of hall
parking=hall//10 # 10% of hall
groom=lunch+breakfast+hall+decorations+parking #total groom
bride=50000
if(bride==groom):
    print("loan not taken")
else:
    bride=groom-bride
    print('loan amount'+bride)
    print("loan has taken")