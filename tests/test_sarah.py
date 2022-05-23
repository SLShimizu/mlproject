from mlproject.sarah import sarah_best

def test_is_sarah_the_best():
    print('Is Sarah really the best')

    assert len(sarah_best()) != 0

    print('yes she is')
