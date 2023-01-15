class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        if flavor not in self.flavors:
            print("Please enter a valid flavor.")
            return

        if scoops > 3 or scoops < 1:
            print("Please enter between 1 and 3 scoops.")
            return

        print("Order Created!")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll pending Ice Cream orders:")
        for cust in self.orders.items:
            print("Customer:", cust["customer"], " -- Flavor:", cust["flavor"], "-- Scoops: ", cust["scoops"])

    def next_order(self):
        print("\nNext order up!")
        dequeued_order = self.orders.dequeue()
        print("Customer:", dequeued_order["customer"], " -- Flavor:", dequeued_order["flavor"], "-- Scoops: ", dequeued_order["scoops"])



shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
