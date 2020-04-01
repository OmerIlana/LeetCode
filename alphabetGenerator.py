import random

def generateRandom(weight_mapping):
    processed_weight_mapping = []
    for curr_char, curr_weight in weight_mapping.items():
        for _ in range(curr_weight):
            processed_weight_mapping.append(curr_char)

    return random.choice(processed_weight_mapping) if len(processed_weight_mapping) else None    


weight_mapping = { "a":1, "b":2, "c":3}
print(generateRandom(weight_mapping))