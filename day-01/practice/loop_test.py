for i in range(5):
    env = input("Please enter your environment (e.g., dev, test, stage, prod): ")
    print("You have entered the environment:", env)
    if env.lower() == "prod":
        print("Warning: You are in the production environment...Don't deploy on Friday!")
    elif env.lower() == "staging":
        print("You are in the staging environment. Take Backup & Test Well. Safe To Deploy Any Day!.")
    else:
        print("You are in the", env, "environment. Safe To Deploy Any Day!.")