class RewardsSystem:
    def __init__(self):
        self.points = 0
    
    def calculate_points(self, emissions):
        if emissions < 5:
            self.points += 10
        elif emissions < 10:   
            self.points += 5
        else: 
            self.points += 1
        return self.points

    def get_reward(self):
        # Determine type of reward based on points
        if self.points >= 1000:
            return 'Free Meal Coupon'
        elif self.points >= 500:
            return '50% off store purchase'
        else:
            return 'Not enough points yet!'

# List of fun facts to award students 
fun_fact = []

def get_fact():
    import random
    return random.choice(fun_fact)

# Request user input to show example usage

reward_system = RewardsSystem()
food_item = input("Food category: ") 
    
emissions = 0

while food_item != "Vegetable" and food_item != "Meat" and food_item != "Fruit":
    if food_item == "Vegetable":
        emissions += 2
    elif food_item == "Meat":
        emissions += 10
    elif food_item == "Fruit":
        emissions += 4
    else:
        emissions += 0

if food_item not in data['food_item']:
    print("Food item not found")
        
reward_system.calculate_points(emissions)
reward = reward_system.get_reward()
fact = get_fact()

print(f"Reward: {reward}")
print(f"Fun Fact: {fact}")