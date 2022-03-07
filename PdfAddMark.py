import codecs
import re

from PyPDF2 import PdfFileMerger, PdfFileReader


class BookMarks(object):
    def add_mark(self, old_pdf_name, marks, new_pdf_name=None):
        pdf_in = PdfFileReader(old_pdf_name)
        pdf_out = PdfFileMerger()
        pdf_out.append(pdf_in, import_bookmarks=False)
        # 通过vis记录其父书签是谁
        vis = {0: None}
        last = 0
        for node in marks:
            vis[node[2]] = pdf_out.addBookmark(node[0], node[1], vis[node[2] - 1])
            print("成功添加%d级书签:%s  页数:%d" % (node[2], node[0], int(node[1])))
        if not new_pdf_name:
            new_pdf_name = old_pdf_name[:-4] + "-书签版.pdf"
        pdf_out.write(new_pdf_name)

    def take_marks(self, marks_path):
        invalid_page = 0
        pre_grade = 0
        marks = []
        for line in codecs.open(marks_path, 'r', encoding='utf-8'):
            line = line.strip()
            if line.startswith('**'):
                try:
                    invalid_page = int(line[2:])
                except ValueError:
                    print("无效页数书写格式有误！")
                continue
            mark = re.match(r'(\+*)\s*?"([^"]+)"\s*\|\s*(\d+)', line)
            if mark:
                grade, title, page_num = mark.groups()
                cur_grade = len(grade)
                cur_node = (title, int(page_num) - 1 + int(invalid_page), cur_grade, [])

                if not (0 < cur_grade <= pre_grade + 1):
                    raise Exception('%s 中字符\'+\'的数量是无效的！' % line)
                else:
                    marks.append(cur_node)
                    pre_grade = cur_grade
            else:
                print("书签格式错误！")

        return marks
