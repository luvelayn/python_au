separator = '<!-----solution----->'


class LeetcodeMaker:
    def __init__(self, title, link, code):
        self.title = title.rstrip('\n').split('. ')[1]
        self.link = link.rstrip('\n')
        self.code = code

    def __str__(self):
        return 'title = {}, link = {}, code = {}'.format(self.title, self.link, self.code)

    def md_title(self):
        return '## {}'.format(self.title)

    def md_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[30:-1])

    def md_code(self):
        return '```python\n{}\n```'.format('\n'.join(map(lambda x: x.rstrip('\n')[4:], self.code)))

    def md_formatted(self):
        return '{}\n{}\n\n{}\n\n{}\n\n{}'.format(self.md_link(), separator, self.md_title(), self.link, self.md_code())


def read_all_lines(file_directory):
    file = open(file_directory)
    result = file.readlines()
    file.close()
    return result


def write_md(file_directory, content):
    file = open(file_directory, 'w')
    file.write(content)
    file.close()


def read_full(file_directory):
    file = open(file_directory)
    result = file.read()
    file.close()
    return result


def merge(old_solution, new_solution):
    old_splitted = old_solution.split(separator)
    if len(old_splitted) <= 1:
        return new_solution
    return '{}{}{}'.format(old_splitted[0], new_solution, old_splitted[1])


def main(source, destination):
    text = read_all_lines(source)
    source_for_md = LeetcodeMaker(text[0], text[1], text[3:])
    new_solution = source_for_md.md_formatted()
    old_solutions = read_full(destination)
    result = merge(old_solutions, new_solution)
    write_md(destination, result)


if __name__ == '__main__':
    main(r"D:\au\python_au\leetcode\source_leetcode_data.txt", r"D:\au\python_au\leetcode\math.md")
