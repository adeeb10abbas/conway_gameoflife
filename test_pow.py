#The Normal Python Function
def pow1(a,b):
    return a**b
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow2(a,b):
    total=1
    for i in range(0,b):
        total=total*a
    return total
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow3(a,b):
    if b==0:
        return 1
    elif b%2==1:
        return a*pow3(a,b-1)
    else:
        temp=pow3(a,b//2)
        return temp*temp

####### Pow 1 tests below

def test_pow1_a():
    assert pow1(0, 1) == 0**1
    assert pow1(1, 0) == 1**0

def test_pow1_b():
    assert pow1(51, 16) == 51**16
    assert pow1(10, 10) == 10**10

def test_pow1_c():
    assert pow1(3, 100) == 3**100
    assert pow1(6, 100) == 6**100

def test_pow1_d():
    assert pow1(21, 21) == 21**21
    assert pow1(12, 12) == 12**12

def test_pow1_e():
    assert pow1(99, 100) == 99**100
    assert pow1(10, 134) == 10**134

####### Pow 2 tests below

def test_pow2_a():
    assert pow2(0, 1) == 0**1
    assert pow2(1, 0) == 1**0

def test_pow2_b():
    assert pow2(51, 16) == 51**16
    assert pow2(10, 10) == 10**10

def test_pow2_c():
    assert pow2(3, 100) == 3**100
    assert pow2(6, 100) == 6**100

def test_pow2_d():
    assert pow2(21, 21) == 21**21
    assert pow2(12, 12) == 12**12

def test_pow2_e():
    assert pow2(99, 100) == 99**100
    assert pow2(10, 134) == 10**134

####### Pow 3 tests below

def test_pow3_a():
    assert pow3(0, 1) == 0**1
    assert pow3(1, 0) == 1**0

def test_pow3_b():
    assert pow3(51, 16) == 51**16
    assert pow3(10, 10) == 10**10

def test_pow3_c():
    assert pow3(3, 100) == 3**100
    assert pow3(6, 100) == 6**100

def test_pow3_d():
    assert pow3(21, 21) == 21**21
    assert pow3(12, 12) == 12**12

def test_pow3_e():
    assert pow3(99, 100) == 99**100
    assert pow3(10, 134) == 10**134