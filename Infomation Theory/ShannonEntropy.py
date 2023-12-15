import math


def shannon_entropy(probabilities):
    """
    Calculate the entropy of a random variable X with given probabilities.

    Parameters:
    probabilities (list): List of probabilities for each outcome of the random variable.

    Returns:
    float: Entropy of the random variable.
    """
    entropy_value = 0
    for p in probabilities:
        if p > 0:
            entropy_value += -p * math.log2(p)
    return entropy_value

def Bernoulli_distribution(p):
    '''
    In a Bernoulli distribution, there are two possible outcomes,
    typically labeled as 0 and 1, with probabilities p and 1−p respectively.
    '''
    return [p,1-p]

def shannon_entropy(probabilities):
    """
    Calculate the entropy of a random variable X with given probabilities.

    Parameters:
    probabilities (list): List of probabilities for each outcome of the random variable.

    Returns:
    float: Entropy of the random variable.
    """
    entropy_value = 0
    for p in probabilities:
        if p > 0:
            entropy_value += -p * math.log2(p)
    return entropy_value


if __name__ == "__main__":
    # Example usage:
    # Replace the probabilities_list with the actual probabilities for your random variable
    Bernoulli_distribution_of_X = Bernoulli_distribution(1/3)
    result_entropy = shannon_entropy(Bernoulli_distribution_of_X)
    print(f'Shannon Entropy: {result_entropy}')
