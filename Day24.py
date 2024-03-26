def register_check(register):
    
    Present = []
    attendance = [u for u in register.values()]  
    for remark in attendance:
        if remark == 'yes':
            Present.append(remark)
    count = len(Present)
    return f"The number of student present is {count}"
        
#Register 
register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
register_check(register)