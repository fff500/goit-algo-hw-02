from queue import Queue


queue = Queue()

def generate_request(number):
    request = input("Введіть заявку: ")
    queue.put(request)
    print(f"Заявка {number}. '{request}' додана до черги.")

def process_request():
    while not queue.empty():
        current_request = queue.get()
        print(f"Обробляємо заявку {current_request}")

    print("Черга пуста, немає заявок для обробки.")

def main():
    for i in range(5):
        generate_request(i + 1)

    process_request()

if __name__ == "__main__":
    main()
