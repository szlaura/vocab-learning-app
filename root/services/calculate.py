from random import randint


def get_random_vocab_number(input_vocab):
    count = len(input_vocab)
    random_num = randint(0, count - 1)
    return random_num
