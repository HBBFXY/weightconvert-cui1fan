def weight_convert():
  s = input().strip()
if s.endswith("kg):
  kg = float(s[:-2])
  pd = kg*2.2046
  print("对应的英制重量为{：.3f}磅".format(pd))
elif s.endswith("pd"):
  pd_val = float(s[:-2])
  kg_val = pd_val /2.2046
  print("对应的公制重量为{:.3f}公斤".format(kg_val))
else:
  printf("输入格式错误，请以kg或pd结尾")这个文件下编写代码，题目具体要求见README.md文件
