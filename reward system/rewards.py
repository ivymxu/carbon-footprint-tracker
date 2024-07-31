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

        return self.rewards

    def get_reward(self):
        # determine type of reward based on points

        return self.rewards

# List of fun facts to award students 
fun_fact = []

def get_fact():
    import random
    return random.choice(fun_fact)

# Request user input to show example usage

reward_system = RewardSystem()
food_item = input("Food item: ") 
    # if statements to determine food item emissions
emissions = get_emissions(food_item) 
reward_system.calculate_points(emissions)
reward = reward_system.get_reward()
fact = get_random_fact()

print(f"Reward: {reward}")
print(f"Fun Fact: {fact}")