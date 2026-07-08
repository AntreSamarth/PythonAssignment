import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter

    for i in range(1000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():
    T1 = threading.Thread(target=Increment, name="Thread1")
    T2 = threading.Thread(target=Increment, name="Thread2")
    T3 = threading.Thread(target=Increment, name="Thread3")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final value of Counter:", Counter)

if __name__ == "__main__":
    main()