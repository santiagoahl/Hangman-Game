from os import system
from random import choice

def read_file(path):
    data = []
    with open(path, 'r', encoding = 'utf-8') as f:
        for line in f:
            data.append(line)
    return data

def print_file(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        for line in f:
            print(line)

def run():
    #Initial values
    data_path = './files/data.txt'
    paths = ['./files/draws/'+str(i)+'.txt' for i in range(11)]
    data = read_file(data_path)
    correct_word = choice(data)
    n_attempts = 9
    current_path = paths[0]
    for i in range(n_attempts):
        
    #canvas   
    

if __name__ == '__main__':
    run()