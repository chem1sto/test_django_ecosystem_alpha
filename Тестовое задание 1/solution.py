def get_n_first_elements(n: int) -> str:
    return "".join([str(_) * _ for _ in range(1, n + 1)])


if __name__ == "__main__":
    print(get_n_first_elements(int(input())))
