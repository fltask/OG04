def hello(name):
    print(f"Hello {name}")


def question():
    answer = input("How old are you?\n")
    return answer


if __name__ == "__main__":
    hello("Dima")
    print(question())
