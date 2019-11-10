def cashToBeRetrun(mrp,cust):
    my_dict={.01:'PENNY',.05:'NICKEL',.10:'DIME',.25:'QUARTER',.50:'HALF DOLLAR',
            1.00:'ONE',2.00:'TWO',5.00:'FIVE',10.00:'TEN',20.00:'TWENTY',50.00:'FIFTY',
            100.00:'ONE HUNDRED'}
    if cust < mrp:
        return 'Error'
    if cust ==  mrp:
        return 'Zero'
    if cust > mrp:
        change= (cust - mrp)
        change= round(change,3)
        print(change)
        results= set([])

    for value in values:
        while change >= value:
            results.add(value)
            change = round((change - value),2)
            print(change)
    #return results
    results =list(results)
    return([my_dict[i] for i in results])
values = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
print(cashToBeRetrun(15.84,16.00))