def test_convert_c_to_f():
    from temp_conversion_module import convert_C_to_F
    answer = convert_C_to_F(50)
    expected = 122
    assert answer == expected
    
def test_2():
    from temp_conversion_module import convert_C_to_F
    answer=convert_C_to_F(-40)
    expected = -40
    assert answer==expected
    
def test_fever_detection():
    from temp_conversion_module import fever_detection
    temp_list = [93.0,98.0,100.0,105.0,"101.0"]
    max_temp, is_fever = fever_detection(temp_list)
    expected_max=105.0
    is_fever = True
    
    assert max_temp == expected_max