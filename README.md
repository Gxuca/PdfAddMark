# PdfAddMark
利用python库PyPDF2对电子书(pdf)快速添加书签

## mark.txt书写格式

- 如果你的`PDF`文件有无效页（比如电子书的前言等），可以在`mark.txt`文件的第一行按照以下结构书写：`**10`
- 书签格式为`+'第一章 这个是一个例子'|1`,+的数量决定其书签的父子关系（父与子之前相差一个+，不可多写），`''`包含目录名，`|`后为目录页上的页码

可参考仓库中的`mark.txt`

## 鸣谢

- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [RuseellLuo](https://github.com/RussellLuo/pdfbookmarker)
