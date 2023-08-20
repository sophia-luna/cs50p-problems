from um import count

def test_count():
    assert count("um, hello, um, world, um")==3
    assert count("yummy yum")==0
    assert count("um...")==1
    assert count("um? thankyum")==1
    assert count("UM.. um")==2