import os
import numpy as np
import pandas as pd
import tensorflow as tf


def process_names(raw_names):
    """ Processes the names to be used as inputs for the model. Spaces are
    changed by 0, hyphens by 1 and end of names are delimited by 2 """
    names = []
    for name in raw_names:
        name = name.lower()
        if ' ' in name:
            name = '0'.join(name.split())
        if '-' in name:
            name = '1'.join(name.split('-'))
        name += '2'
        names.append(name)
    return names


def load_tokenizer(names):
    """ Creates a tokenizer and tokenizes the names. """
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=43)
    for name in names:
        tokenizer.fit_on_texts(list(name))
    return tokenizer


def build_name(out_name):
    """ Transforms output of the model into names. """
    name = []
    for c in out_name:
        if c == '0':
            name.append(' ')
        elif c == '1':
            name.append('-')
        elif c != ' ':
            name.append(c)
    name = ''.join(name)
    return ' '.join([n.capitalize() for n in name.split()])


def generate_name(tokenizer, input_name=''):
    """ Given a sequence of characters, computes its continuation using the trained model. """
    while True:
        gen_name = input_name
        gen_name = gen_name.lower()
        gen_name = '0'.join(gen_name.split(' '))  # 0: Spaces
        gen_name = '1'.join(gen_name.split('-'))  # 1: Hyphens
        char = ''
        while char != '2':  # 2: End of name
            token_list = tokenizer.texts_to_sequences([' '.join(gen_name)])
            token_list = tf.keras.preprocessing.sequence.pad_sequences(token_list, max_len - 1)
            predicted = np.random.choice(range(0, total_char), p=model.predict(token_list)[0])
            for char, index in tokenizer.word_index.items():
                if index == predicted:
                    if char == '2':
                        break
                    gen_name += ' ' + char
        gen_name = build_name(gen_name)
        if gen_name not in raw_names:
            break
    return gen_name


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    model = tf.keras.models.load_model('model/model.h5')
    data = pd.read_csv('data/Tolkien_characters.csv')
    raw_names = data['Name'].to_list()
    names = process_names(raw_names)

    max_len = max((len(s) for s in raw_names))
    total_len = sum((len(s) for s in raw_names))
    different_char = set(''.join(names))
    total_char = len(different_char)

    tokenizer = load_tokenizer(names)

    print('Press ENTER to generate a new name. You can also provide with its beginning. The model will complete it.')
    while True:
        input_name = input('> ')
        gen_name = generate_name(tokenizer, input_name)
        print(f'* {gen_name}')
