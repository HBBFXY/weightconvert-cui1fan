weight_input = input()
num = float(weight_input[:-2])
unit = weight_input[-2:]
if unit =="kg":
  pound = num * 2.2046
  print(f"对应的英制重量单位为{pound:.3f}磅")
elif unit =="pd":
  kg = num / 2.2046
  print(f"对应的公制重量为{kg:.3f}公斤")# 在这个文件下编写代码，题目具体要求见README.md文件
