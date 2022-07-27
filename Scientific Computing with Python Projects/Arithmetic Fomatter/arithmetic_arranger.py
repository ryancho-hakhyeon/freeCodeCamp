class OperatorError(Exception):
    """ Raise Operrator Error if operator is not '+' or '-' """
    pass


class ValueLengthError(Exception):
    """ Raise Error if each value is longer than 4 """
    pass

def display_form(f_nums, s_nums, operators):
    n = len(f_nums)
    space = "    "
    first_line, second_line, third_line = "", "", ""
    results = ""

    for i in range(n):
        maxLen = max(len(f_nums[i]), len(s_nums[i]))
        ffront_spaceLen = maxLen - len(f_nums[i]) + 2
        sfront_spaceLen = maxLen - len(s_nums[i]) + 1
        third_spaceLen = maxLen + 2

        if operators[i] == '+':
            res = str(int(f_nums[i]) + int(s_nums[i]))
        else:
            res = str(int(f_nums[i]) - int(s_nums[i]))

        res_spaceLen = (maxLen + 2) - len(res)

        if i != n - 1:
            first_line += (" " * ffront_spaceLen + (f_nums[i] + space))
            second_line += (operators[i] + (" " * sfront_spaceLen) + (s_nums[i] + space))
            third_line += (("-" * third_spaceLen) + space)
            results += ((" " * res_spaceLen) + res + space)
        else:
            first_line += (" " * ffront_spaceLen + f_nums[i])
            second_line += (operators[i] + (" " * sfront_spaceLen) + s_nums[i])
            third_line += ("-" * third_spaceLen)
            results += ((" " * res_spaceLen) + res)

    return first_line, second_line, third_line, results


def arithmetic_arranger(problems, displayed=False):
        f_nums = []
        s_nums = []
        operators = []
        try:
            if len(problems) > 5:
                raise TypeError
            else:
                for t in problems:
                    f = t.split()

                    if type(int(f[0])) != int or type(int(f[2])) != int:
                        raise ValueError

                    if len(f[0]) > 4 or len(f[2]) > 4:
                        raise ValueLengthError

                    if f[1] != '+' and f[1] != '-':
                        raise OperatorError
                    f_nums.append(f[0])
                    operators.append(f[1])
                    s_nums.append(f[2])

        except TypeError:
            return "Error: Too many problems."
        except ValueError:
            return "Error: Numbers must only contain digits."
        except ValueLengthError:
            return "Error: Numbers cannot be more than four digits."
        except OperatorError:
            return "Error: Operator must be '+' or '-'."

        res = display_form(f_nums, s_nums, operators)

        if displayed:
            return "{}\n{}\n{}\n{}".format(res[0], res[1], res[2], res[3])
        return "{}\n{}\n{}".format(res[0], res[1], res[2])
