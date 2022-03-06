# 扩展语法

## 表格

- 使用3个及以上数量的连字符创建每列标题,并使用管道(` | `)分隔每列
- 单元格的宽度可变化,不影响渲染
- 为了便于使用可以使用[Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)图形界面构建表

## 围栏代码块

- 在代码块之前和之后的行商使用三个反引号```` ``` ````或三个波浪号` ~~~ `

### 语法高亮

- 代码块之前的反引号旁边指定一种语言

```c++
#include <iostream>
using namespace std;
int main()
{
    cout << 1 << endl;
    return 0;
}
```

## 脚注

- 在方括号内添加插入符号` ^ `和标识符,标识符可以时数字或单词,但不能包含空白符,例如` [^1] `

> Here's a simple footnote[^1].
>
> Here's also a footnote[^bignote].
>
> [^1]:This is a footnote.
> [^bignote]:hello

## 标题编号

- 支持标题的自定义ID,允许直接链接到标题并使用CSS对其进行修改,要添加自定义标题,需要在标题相同的行上使用` {} `包裹该自定义ID

> [Heading IDs](#heading-ids)

## 定义列表

- 创建术语及其对应定义的定义列表

> First Term
> : This is the definition of the first term.
>
> Second Term
> : This is one definition of the second term.
> : This is another definition of the second term.

## 删除线

- 在单词或短语前后使用两个波浪号`~~`

## 任务列表

- 创建带有复选框的项目列表,在任务列表之前添加破折号`-`,后加空格,再加上方括号`[]`
- [x] Write the press release
- [ ] Update the website

## 使用Emoji表情

1.复制粘贴表情符号

- 如果使用的是静态网站生成器,需要确保HTML页面编码为UTF-8

2.使用表情符号简码

- 键入表情符号短代码,例如`:tent:`表示:tent:,`:joy:`表示:joy:

## 自动网址链接

- 许多Markdown处理器会自动将URL转换为链接,需要禁用自动URL链接时,使用反引号删除链接
