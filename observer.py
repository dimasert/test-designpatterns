class observer:
    def update(self, subject):
        print("observer: my subject just updated and told me about it")
        print("observer: current status is" + str(subject._state))

class subject:
    _state = 0
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):

        print("im notify my observers....")
        for observer in self._observers:
            observer.update(self)

    def updateState(self,n):

        print("i receive a update status")
        self._state = n

        self.notify()

s = subject()

ob1 = object()
ob2 = object()
ob3 = object()
ob4 = object()

s.attach(ob1)
s.attach(ob2)
s.attach(ob3)
s.attach(ob4)

s.updateState(5)