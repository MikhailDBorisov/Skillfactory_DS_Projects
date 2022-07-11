#Project_1: Guess a random number from 0 to 100 in 20 attempts or less
import numpy as np

def random_predict(number: int=np.random.randint(0,101)) -> int:
    count = 0
    low_bound = 0
    high_bound = 101
    
    while True:    
        count+=1
        guess = np.random.randint(low_bound,high_bound)
        
        if guess == number:
            break
        elif guess>number:
            high_bound=guess
        else:
            low_bound=guess+1
        
    return count

def predict_array(random_predict) -> int:
    
    count_lst = []
    random_array = np.random.randint(0, 101, size=(1000))
    
    for number in random_array:
        count_lst.append(random_predict(number))
    
    mean_count = int(np.mean(count_lst))
    print(f'Mean number of guesses for the algorithm: {mean_count}')
    return mean_count

#RUN
if __name__ == '__main__':
    try_func1 = predict_array(random_predict)
    