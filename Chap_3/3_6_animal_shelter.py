from queue import Queue


class Animal:
    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp

    def __gt__(self, animal2):
        return self.timestamp > animal2.timestamp

    def __eq__(self, animal2):
        return self.timestamp == animal2.timestamp


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.current_time = 0

    def enqueue_dog(self, name):
        """ enquee a dog"""
        self.dogs.add(Animal(name, self.current_time))
        self.current_time += 1

    def enqueue_cat(self, name):
        """ enqueue a cat """
        self.cats.add(Animal(name, self.current_time))
        self.current_time += 1

    def dequeue(self):
        """ dequeue oldest animal"""
        # no dogs nor cats
        if self.dogs.is_empty() and self.cats.is_empty():
            return None

        # no dogs, return the oldest cat
        if self.dogs.is_empty():
            return self.cats.remove().name

        # no cats, return the oldest dog
        if self.cats.is_empty():
            return self.dogs.remove().name

        # return the oldest of the two
        if self.cats.peek() < self.dogs.peek():
            return self.cats.remove().name
        else:
            return self.dogs.remove().name

    def dequeue_dog(self):
        """ dequeue oldest dog"""
        if not self.dogs.is_empty():
            return self.dogs.remove().name

    def dequeue_cat(self):
        """ dequeue oldest cat"""
        if not self.cats.is_empty():
            return self.cats.remove().name


c = AnimalShelter()
c.enqueue_cat("kabongo")
c.enqueue_cat("ppp")
c.enqueue_dog("tshimpaka")

print(c.dequeue_dog())
print(c.dequeue())
print(c.dequeue())
print(c.dequeue())
