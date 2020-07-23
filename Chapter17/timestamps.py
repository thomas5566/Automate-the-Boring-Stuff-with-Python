import time

def calcProd():
    # Caculate the product of the first 100,000 numbers
    product = 1

    for i in range(1, 100000):
        product = product * i

    return product


startTime = time.time()
prod = calcProd()

endTime = time.time()

print('The result is {} digitd long.'.format(len(str(prod))))
print('Took {} seconds to calculate.'.format(endTime - startTime))

