def simulate_history(actions):
    """
    Process a list of actions for a drawing app and apply UNDO behavior.

    :param actions: list of strings; "UNDO" means remove the most recent action
    :return: list of strings representing the remaining actions
    """

    stack = []  # this will hold active actions

    for action in actions:
        if action == "UNDO":
            # pop only if the stack isn't empty
            if stack:
                stack.pop()
        else:
            # push regular action
            stack.append(action)

    return stack