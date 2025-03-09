from mail import check_email
#always have to import for unit testing

def test_check_email():
    assert check_email("example@my.bcit.ca") == True
    assert check_email("somewhere") == False

def test_check_email_bogus():
    assert check_email("yes.no@mybcit") == False