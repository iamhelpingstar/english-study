path = "copied_text.md"
answer_list = []
is_answer = False
with open(path, "r") as file:
    for line in file:
        if line == 'ChatGPT\n':
            is_answer = True
            continue
        elif line == 'User\n':
            is_answer = False
            continue
        elif line == '\n':
            continue
        if is_answer:
            answer_list.append(line)

with open(path, "w") as file:
    for sen in answer_list:
        file.write(sen)
        file.write('\n')
