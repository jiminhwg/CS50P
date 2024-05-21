from project import loading_screen, intro, question1, question2, question3, End

#pytest -s test_project.py <--- https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html

def test_loading_screen():
    assert loading_screen() == True

def test_intro():
    assert intro("name") == True

def test_question1():
    assert question1("name") == 1

def test_question2():
    assert question2("name") == 2

def test_question3():
    assert question3("name") == 3

def test_end():
    assert End("name") == "Bye!"
