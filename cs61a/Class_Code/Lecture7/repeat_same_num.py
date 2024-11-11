def repeat(k):
    """When called repeatedly, print each repeated argument
    >>>f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    
    """
    return detector(lambda j: False)(k)
    
def detector(repeat_check):
    def input_num(x1):
        if repeat_check(x1):
            print(x1)
        return detector(lambda y: x1 == y or repeat_check(y))
    return input_num
    