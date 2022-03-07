from PdfAddMark import BookMarks


def main():
    work = BookMarks()
    # 将pdf、书签文件放到main.py的同级目录
    work.add_mark("计算机组成原理.pdf", work.take_marks("mark.txt"))


if __name__ == '__main__':
    main()
