import multiprocessing



#run this in background
def square_list(my_list,result,square_sum):
    for idx,i in enumerate(my_list):
        result[idx] = (i*i)
        
    square_sum.value = sum(result)
    print(f"result in sub process {result[:]}")
    print(f'sum of squares in sub process  {square_sum.value}')
    
if __name__ == "__main__":
    my_list = [100,200,300,400]
    result = multiprocessing.Array("i",4)
    square_sum = multiprocessing.Value("i")
    cp1 = multiprocessing.Process(target = square_list,args=(my_list,result,square_sum))
    cp1.start()
    print("In main processs.......I am doing something......")
    cp1.join()
    print(f"Result in main program is {result[:]}")
    print(f'sum of squares in sub process  {square_sum.value}')
    
