def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    updated = []

    for s in range(len(values)):
        best_value = float("-inf")

        for a in range(len(transitions[s])):
            action_value = rewards[s][a]

            for next_state, probability in enumerate(transitions[s][a]):
                action_value += gamma * probability * values[next_state]

            best_value = max(best_value, action_value)

        updated.append(float(best_value))

    return updated