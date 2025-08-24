class picnic:
    def __init__(self,frnds_areas,places,budget):
        self.frnds_areas=frnds_areas
        self.places=places
        self.budget=budget
        
    def pick_up(self):
        print("picking up friends:")
        for frnd,area in self.frnds_areas.items():
            print(f" picked up {frnd} from {area}")

        print(" now visiting places together:")
        for place in self.places:
            print(f" went to {place}")

    def money(self):
        extra_charges=40000
        Totall= self.budget + extra_charges # self.budget is int value so use + if it is list use sum()
        if Totall <= 100000:
            print(" we are good")
        else:
            print(" we are spending so much of money")
    def shopping(self,each_shopping):
        self.each_shopping=each_shopping
        for friend_dict  in self.each_shopping:
            for friend ,items  in friend_dict.items():
                print(f"{friend} bought : {', '.join(items)}")
                
            
frnds_areas={"sita":"kadapa","gita":"rajempeta","ram":"tirupati"}
places=["tirumala","arunachalam","tirutani"]
budget=80000
each_shopping=[{"sita":["sacred threads","laddus","some idols"]},{"gita":["sacred threads","laddus","dhoop sticks"]},{"ram":["laddus"]}]
start=picnic(frnds_areas,places,budget)
start.pick_up()
start.money()
start.shopping(each_shopping)

