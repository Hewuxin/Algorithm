"""
字符串转数字

"""


def str_to_int(string):
    # 1. 如果字符串为空
    if not string:
        return
    # 2. 非法输入
    if len(string) > 10:
        return "string too long"

    # 负数
    num_f = False
    if string[0] == "-":
        num_f = True
        string = string[1:]
    # 正数
    count = 1
    num = 0
    for item in string[::-1]:
        if '0' <= item <= "9":
            num += int(item) * count
            count = count * 10
        else:
            break
    # 3. 溢出 -2**32～ 2**32 -1
    if num_f:
        num = 0 - num
    return num


class Solution:
    def myAtoi(self, s: str) -> int:
        # 如果s为空 或者
        if s == "":
            return 0
        # s只有一个字符且不在0～9之间
        if len(s) < 2 and not ("0" <= s <= "9"):
            return 0
        # 前提是没有空格后面遇到非法输入就停止
        i = 0
        is_neg = False
        res = 0
        # 判断string是否全空
        while i < len(s) and s[i] == " ":
            i += 1
        # 此时string全空
        if i == len(s):
            return 0
        # 如果是-开头 表示为负数
        if s[i] == "-":
            is_neg = True
            # s = s[i + 1:]
            i += 1
        elif s[i] == "+":
            i += 1
        # 声明一个用来存放真正可以输出的数
        res_list = list()
        for item in s[i:]:  # 最多O(n)
            if "0" <= item <= "9":
                res_list.append(item)
            else:
                break
        # "123" --》 1 * （10**2）
        # index=0 length=3 length-index-1
        # 考虑到越界问题 -2**32 ~ 2**31 将正数作为负数处理，之后根据是否为正数 重新回正
        for index, value in enumerate(res_list):
            if res <= - 2 ** 32:
                res = -2 ** 32
                break
            res -= int(value) * (10 ** (len(res_list) - index - 1))
        if not is_neg:
            res = 0 - res

        return min(max(res, -2 ** 31), 2 ** 31 - 1)


if __name__ == '__main__':
    # print(str_to_int("123"), type(str_to_int("123")))
    # print(str_to_int("123.123"), type(str_to_int("123.213")))
    # print(str_to_int("+22"), type(str_to_int("+22")))
    # print(str_to_int("-22"), type(str_to_int("-22")))
    # print(" - ", str1("-"), type(str1("-")))
    # print(str_to_int("-42949672961"), type(str_to_int("-42949672961")))

    # print(str1("123"), type(str1("123")))
    # print(str1("123.123"), type(str1("123.213")))
    # print(str1("+22"), type(str1("+22")))
    # print(str1("-22"), type(str1("-22")))
    # print(str1("-"), type(str1("-")))
    # print(str1("-42949672961"), type(str1("-42949672961")))
    print(len("  "))
    print(str1("  "), type(str1("  ")))
