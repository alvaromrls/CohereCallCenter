import requests

newConversation = """Press:
- N to see next log page
- P to see prev log page
- [1-5] to select a log
- Any other key to skip
 """

whatToDoConversation = """--- OK, now press:
--- D to delete it
--- A to assign a group
--- Any other key to return
---
"""


class client:
    def __init__(self):
        self.get_data()
        self.categories = list(
            requests.get("http://localhost:5000/metadata").json().keys()
        )
        print(self.categories)

    def get_data(self):
        self.data = requests.get("http://localhost:5000/logs").json()
        self.page = 0
        self.total_data = len(self.data)
        if self.total_data > 5:
            self.page_numbers = [1, 2, 3, 4, 5]
        else:
            self.page_numbers = list(range(1, self.total_data + 1))

    def printdata(self):
        print(f"Messages in the log {self.page_numbers[0]}-{self.page_numbers[-1]}: ")
        ind = 1
        for i in self.page_numbers:
            print(f"{ind}: {self.data[i-1]}")
            ind += 1

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.page_numbers = list(range(self.page * 5 + 1, (self.page + 1) * 5 + 1))

    def next_page(self):
        if self.page_numbers[-1] < self.total_data:
            self.page += 1
            if self.total_data > (self.page + 1) * 5:
                self.page_numbers = list(
                    range(self.page * 5 + 1, (self.page + 1) * 5 + 1)
                )
            else:
                self.page_numbers = list(range(self.page * 5 + 1, self.total_data + 1))

    def print_categories(self):
        index = 1
        print("------Select the cateogorie")
        for cat in self.categories:
            print(f"------{index}: {cat}")
            index += 1

    def loop(self):
        while True:
            self.printdata()
            k = input(newConversation).strip()
            if k in ["N", "n"]:
                self.next_page()
            elif k in ["P", "p"]:
                self.prev_page()
            elif k in ["1", "2", "3", "4", "5"]:
                option = input(whatToDoConversation).strip()
                if option in ["D", "d"]:
                    print("Deleting items in the server ...")
                    # requests.delete(
                    print(f"http://localhost:5000/logs/{self.page_numbers[int(k)]-1}")
                    # )
                    self.get_data()
                elif option in ["A", "a"]:
                    self.print_categories()
                    try:
                        categorie_index = input()
                        categorie = self.categories[int(categorie_index) - 1]
                        requests.patch(
                            f"http://localhost:5000/logs/{self.page_numbers[int(k)]-1}",
                            data={"category": categorie},
                        )
                        self.get_data()
                    except:
                        print("Ops.. something went wrong")
            else:
                break
