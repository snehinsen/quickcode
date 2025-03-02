option = int(input("Simple or compound interest? (1, 2): "))

if option == 1:
    principle = float(input("PPrinciple: "))
    rate = float(input("Rate (%): "))
    time = float(input("Time: "))
    interest = principle * rate * time / 100
    print("Simple interest: ", interest)
    principle += interest
    print("Amount: ", principle)

if option == 2:
    principle = float(input("PPrinciple: "))
    rate = int(input("Rate (%): "))
    time = int(input("Time: (years)"))
    principle2 = principle
    interest = 0
    totalInterest = 0
    for i in range(time):
        interest = principle * rate / 100
        totalInterest += interest
        principle += interest

    print("Interest: ", totalInterest)

    print(f"Amount: {(principle2 + totalInterest):.2f}")
