from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    test_result = text_to_duration(input_value)
    assert text_to_duration(input_value) == 10 # built in keywork to run the assumption that something returns a T/F value
    print(f"text_to_duration('10:00') == 10?", {test_result})



    test_text_to_duration_integer()