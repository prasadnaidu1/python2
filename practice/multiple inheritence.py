class Q:
    def __init__(self):
        print('i am Q construter')
        super().__init__()
class P(Q):
    def __init__(self):
        print('i am P construter')
        super().__init__()
class R:
    def __init__(self):
        print('i am R construter')
        super().__init__()
class X(P,R):
    def __init__(self):
        print('i am x construter')
        super().__init__()
class S:
    def __init__(self):
        print('i am S construter')
        super().__init__()
class T:
    def __init__(self):
        print('i am T construter')
        super().__init__()
class U(S,T):

    def __init__(self):
        print('i am U construter')
        super().__init__()
class Y(U):
    def __init__(self):
        print('i am Y construter')
        super().__init__()
class Z(X,Y):
    def __init__(self):
        print('i am Z construter')
        super().__init__()
zobj=Z()
print(Z.mro())

1