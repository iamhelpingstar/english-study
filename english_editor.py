from typing import Deque
import re
from collections import deque

READ = "@@@"
EDIT = "==="

REPEAT = 10


def contains_korean(text):
    korean_regex = re.compile(r"[가-힣]")
    return bool(korean_regex.search(text))


def contains_r_number(text):
    pattern = re.compile(r"\[R\s+(\d+)\]")
    match = pattern.search(text)
    return int(match.group(1)) if match else None


def r_nubmer(n: int) -> str:
    return f"[R {n}]"


def write_edit(n: int, q: Deque[str]):
    path = f"sentence/edit.md"
    with open(path, "a") as file:
        file.write(r_nubmer(n))
        file.write("\n\n")
        while q:
            file.write(q.popleft())
            file.write("\n\n")


def write_non_read(n: int, q: Deque[str]):
    path = f"sentence/r{n}.md"
    with open(path, "w") as file:
        while q:
            file.write(q.popleft())
            file.write("\n\n")


def write_read(n: int, q: Deque[str]):
    path = f"sentence/r{n+1}.md"
    with open(path, "a") as file:
        while q:
            file.write(q.popleft())
            file.write("\n\n")


def edit_to_r():
    r_number = None
    r_list = [[] for _ in range(REPEAT)]
    with open("sentence/edit.md", "r") as e_file:
        for e_line in e_file:
            e_line = e_line.rstrip()
            if e_line == "":
                continue
            if contains_r_number(e_line) is not None:
                r_number = contains_r_number(e_line)
                continue
            else:
                r_list[r_number].append(e_line)

    for i in range(REPEAT):
        if not r_list[i]:
            continue
        with open(f"sentence/r{i}.md", "a") as r_file:
            for line in r_list[i]:
                r_file.write(line)
                r_file.write("\n\n")
    open(f"sentence/edit.md", "w").close()


def get_all_sentences(n: int) -> Deque[str]:
    path = f"sentence/r{n}.md"
    sentences = deque()
    with open(path) as file:
        for line in file:
            line = line.rstrip()
            if line == "":
                continue
            sentences.append(line)
    return sentences


def move_sentences(n: int):
    s_arr = get_all_sentences(n)
    not_read_zone = True
    edit_arr = deque()
    not_read_arr = deque()
    read_arr = deque()

    while s_arr:
        sen = s_arr.pop()
        if sen in {READ, EDIT}:
            assert contains_korean(s_arr[-1]), f"{n}, {s_arr[-1]}"
            if sen == READ:
                not_read_zone = False
                continue
            if sen == EDIT:
                edit_arr.appendleft(s_arr.pop())
                edit_arr.appendleft(s_arr.pop())
                continue
        if not_read_zone:
            not_read_arr.appendleft(sen)
        else:
            read_arr.appendleft(sen)
    return not_read_arr, read_arr, edit_arr


if __name__ == "__main__":
    final_not_read_arr = []
    final_read_arr = []
    final_edit_arr = []

    for i in range(REPEAT):
        not_read_arr, read_arr, edit_arr = move_sentences(i)
        final_not_read_arr.append(not_read_arr)
        final_read_arr.append(read_arr)
        final_edit_arr.append(edit_arr)

    for i in range(REPEAT):
        if final_edit_arr[i]:
            write_edit(i, final_edit_arr[i])

    for i in range(REPEAT):
        write_non_read(i, final_not_read_arr[i])

    for i in range(REPEAT):
        write_read(i, final_read_arr[i])

    ans = input("edit finish?")
    if ans == "y":
        edit_to_r()
    else:
        print("edit not finish")
