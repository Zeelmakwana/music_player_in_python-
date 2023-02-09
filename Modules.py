import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak(t):
    engine.setProperty('rate', 130)
    engine.say(t)
    engine.runAndWait()


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nLts..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        qu = r.recognize_google(audio, language="en-In")
        print("Ok!")
    except Exception as e:
        return ""
    return qu


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class cdll:
    def __init__(self):
        self.first = None

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)

    def display(self):
        if self.first is None:
            return
        current = self.first
        print("Doubly Linked List:")
        while True:
            print("<---{}--->".format(current.data), end=' ')
            current = current.next
            if current == self.first:
                break
