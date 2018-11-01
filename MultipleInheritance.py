class A:
    def A(self):
        print ("I am A")


class B:
    def A(self):
        print("I am B.A")

    def B(self):
        print("I am B")


class C(A,B):
    def C(self):
        print("I am C")

class D(B,A):
    def D(self):
        print("I am D")

c_obj = C()
c_obj.A()
c_obj.B()

d = D()
d.A()


# I am A
# I am B
# I am B.A
