from unittest.mock import patch



def method_name():
    import sut_pkg2
    assert sut_pkg2.sut(1) == 2
    return sut_pkg2.sut

def test_foo():
    print("orig invoke")
    orig = method_name()
    print("mocked invoke")
    # Mock sut() in sut()
    with patch('sut_pkg2.sut') as mck:
        mck.return_value=-1
        assert orig(1) == 0 # (+1-1)



