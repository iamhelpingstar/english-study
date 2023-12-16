import re
from collections import deque

path = "copied_text.md"
answer_q = deque()
is_answer = False


def contains_korean(text):
    korean_regex = re.compile(r"[가-힣]")
    return bool(korean_regex.search(text))


with open(path, "r", encoding="UTF-8") as file:
    for line in file:
        if line == "ChatGPT\n":
            is_answer = True
            continue
        elif line == "User\n":
            is_answer = False
            continue
        elif len(line) < 10:
            continue
        elif line == "\n":
            continue
        if is_answer:
            answer_q.append(line)

answer_dict = {}

while answer_q:
    eng = answer_q.popleft()
    kor = answer_q.popleft()
    answer_dict[eng] = kor

with open("after" + path, "w", encoding="UTF-8") as file:
    for eng, kor in answer_dict.items():
        file.write(eng)
        file.write("\n")
        file.write(kor)
        file.write("\n")
