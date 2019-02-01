
def convert_C_to_F(temp_c):


    temp_f=1.8*temp_c+32;

    return temp_f

def fever_detection(temp_list):

    fever_threshold = 100.4
    is_fever = False
    max_temp = 0
    
    for temperature in temp_list:
        if type(temperature)==str:
            number_temp = float(temperature)
        else:
            number_temp=temperature
            
    max_temp=max(number_temp)

    for temperature in number_temp:
        if temperature>fever_threshold:
            is_fever = True
                
    return max_temp, is_fever
                
    
def main(): 
    temp_cstr = (input("Enter temperature in deg C: "))
    temp_c=float(temp_cstr)
    temp_f=convert_C_to_F(temp_c)
    print("The temperature in Fahrenheit is %f" % temp_f)


if __name__=="__main__":
    main()