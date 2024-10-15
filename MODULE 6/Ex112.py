def calculate_health_probability(P_A1, P_B_given_A1, P_A2, P_B_given_A2):

    if not (0 <= P_A1 <= 1 and 0 <= P_A2 <= 1 and 0 <= P_B_given_A1 <= 1 and 0 <= P_B_given_A2 <= 1):
        return "Invalid probability values. They must be between 0 and 1."


    if round(P_A1 + P_A2, 5) != 1:
        return "Invalid event probabilities: P_A1 + P_A2 must equal 1."


    P_B = (P_A1 * P_B_given_A1) + (P_A2 * P_B_given_A2)

    return P_B
P_A1=float(input('Enter P_A1:'))
P_A2=float(input('Enter P_A2:'))
P_B_given_A1=float(input('Enter P_B_given_A1: '))
P_B_given_A2=float(input('Enter P_B_given_A2: '))
print(calculate_health_probability(P_A1,P_B_given_A1,P_A2,P_B_given_A2))