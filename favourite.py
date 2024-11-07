from openai import OpenAI
import random
import os

# Initialize the OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate a random two-digit number
def generate_2_digit_number():
    return random.randint(10, 99)


# Function to generate random triples (A, B, C) sorted by sum of prime factors
def generate_triple():
    A = generate_2_digit_number()
    B = generate_2_digit_number()  # Ensure B < A
    C = generate_2_digit_number()  # Ensure C < B
    return A, B, C

# Function to query OpenAI API about which number it prefers or if one is less than the other
def query_comparison(X, Y):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers with just one number"},
        {"role": "user", "content": f"Which number is your favorite, {X} or {Y}? Respond with just the number"}
    ]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1,
        temperature=0
    )
    
    # Parse response and determine the preference or lesser choice
    answer = response.choices[0].message.content.strip()
    return answer
# Main loop to generate and test triples with randomized query order
def main():
    n = 0
    for _ in range(100):  # Generate and test 100 triples
        A, B, C = generate_triple()
        
        # Define comparison pairs and shuffle them to randomize the query order
        comparisons = [(A, B), (B, C), (C, A)]
        random.shuffle(comparisons)
        
        # Dictionary to store preferences or "less than" results
        preferences = {}
        
        # Perform each comparison in the randomized order
        for X, Y in comparisons:
            preferred = query_comparison(X, Y)
            if preferred:
                preferences[(X, Y)] = preferred

        ab = preferences.get((A, B))
        bc = preferences.get((B, C))
        ca = preferences.get((C, A))
        # Check for cycles in both "greater than" and "less than" patterns

        cycle = len({ab, bc, ca}) == 3

        # Print the triple if any cycle is detected
        if (cycle):
            print(f"Cycle detected in preferences: A={A}, B={B}, C={C}")
            print(f"{ab}, {bc}, {ca}")
            n += 1
        else:
            print(f"Consistent preferences: A={A}, B={B}, C={C}")
            print(f"{ab}, {bc}, {ca}")
    print(f"Number of cycles detected: {n}")

# Run the main function
main()
