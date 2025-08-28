from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    # OPTION 1: the following lines let us visually inspect if the output is right by reading the print statement
    #test_result = text_to_duration(input_value)
    #print(f"text_to_duration('10:00') == 10?", {test_result})
    # OPTION 2: assert is alternative way to force an error if not correct
    assert text_to_duration(input_value) == 10 # built in keyword to run the assumption that something returns a T/F value


def test_text_to_duration_float():
    actual_value = text_to_duration("10:15")
    #print(f"actual value should be {actual_value}")
    assert actual_value == 10.25

def test_text_to_duration_irrational():
    assert abs(text_to_duration("10:20") - 10.33333) < 1e-5 # way to get around evaluating irrational numbers
    #assert text_to_duration("10:20") == 10 + 1/3 # alternate suggestion
