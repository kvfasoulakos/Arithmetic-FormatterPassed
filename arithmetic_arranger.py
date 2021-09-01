import re


def arithmetic_arranger(problems, solve=False):

  if (len(problems) > 5):
    return "Error: Too many problems."


  up_number = ""
  down_number = ""
  lines = ""
  sumx = ""
  new_string = ""
  for problem in problems:
    if(re.search("[^\s0-9.+-]", problem)):
      if(re.search("[/]",problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]


    if (len(firstNumber) >= 5 or len(secondNumber) >=5 ):
      return "Error: Numbers cannot be more than four digits."

    new_sum = ""
    if operator == '+':
      new_sum = str(int(firstNumber) + int(secondNumber))
    elif operator == '-':
      new_sum = str(int(firstNumber) - int(secondNumber))
    
    max_len = max(len(firstNumber),len(secondNumber)) + 2
    top = str(firstNumber).rjust(max_len)
    bottom = operator + str(secondNumber).rjust(max_len-1)
    line = ""
    res = str(new_sum).rjust(max_len)
    for i in range(max_len):
      line += "-"

    if problem != problems[-1]:
      up_number += top + '    '
      down_number += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      up_number += top
      down_number += bottom
      lines += line
      sumx += res

  if solve:
    new_string = up_number + "\n" + down_number +"\n" + lines +"\n" + sumx
  else:
    new_string = up_number + "\n" + down_number +"\n" + lines
    
  return new_string


  

    