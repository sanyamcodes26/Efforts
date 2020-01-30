from tqdm import tqdm, trange
from time import sleep


if __name__ == "__main__":
    '''
    for i in tqdm(range(20)):
        sleep(0.5)
        pass
    
    for i in trange(20):
        sleep(0.1)
        pass
    
    progressbar = tqdm([2, 4, 6, 8, 10, 12, 14, 16])
    for item in progressbar:
        sleep(0.2)
        progressbar.set_description(f"Processing Element : {item}")
    '''
    with tqdm(total=100) as progressbar:
        for i in range(25):
            sleep(0.1)
            progressbar.update(4)

