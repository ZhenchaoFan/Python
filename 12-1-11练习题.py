#
# 习题在最底下， 上面是我做过的， 但实现方法不是最优的， 可以给我一种更简洁的方法  并注上说明。谢谢！
#
# 练习1
# 打印单词'interested'中的每一个字母。
#
aa1 = "interested"
aa1list = list(aa1)
print(aa1list)


#
# 练习2
# 对列表Names = ['Bart', 'Lisa', 'Adam']中的每个名字打印Hello,xxx
#
#

names = ['bart','isa','adam']
# y1 = ("Hello,"+ names[0]+"!")
# y2 = ("Hello,"+ names[1]+"!")
# y3 = ("Hello,"+ names[2]+"!")
# print(y1)
# print(y2)
# print(y3)
#

#  简单点的

for name in names:
    yy6 = "hello," + name + "!"
    print(yy6)
#
# 练习3
# 计算1-100内所有偶数的和。
#
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


#
# 练习4
# 倒序输出列表[1,2,3,4,5]中的元素  .reverse 倒序  .sort 按序列正序排列   .sorted  排序并保留原有列表
#
x = ['1','2','3','4','5']
x.reverse()
print(x)


# 练习5
# 编写代码，使用 if...elif...else 语句判断输入的一个数字是正数、负数或零.
# #  OK了  待完善
age = float(input("请输入数字："))   #  考虑到小数  所以才用了 float

if age == 0:
    print(int(age))
    print("此数是：0")
elif age > 0:
    print(age) #这里 要是输入小数 打印小数是对的，但是我要是输入的是整数 不想要整数后面的 .0该怎么写
    print("此数是正数")
else:
    print("此数为负数")



# 练习6
# 根据输入年龄，对其称谓进行归类： 大于18岁，输出 adult，小于18岁，输出teenager。
# 编写代码，使输出结果为：1
#
# your age is 3
# teenager

age = int(input("请输入实际年龄："))

if age > 18:
    print('成人 adult')
elif age < 18:
    print('少年 teenager')



# 练习7
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻 18.5-25：正常 25-28：过重 28-32：肥胖 高于32：严重肥胖
# 请用代码实现它,并实现输出结果为：
# your bmi is: 26.285714285714285
# 过重
#
xm_name = 80.5/1.75 ** 2
print(xm_name)

tizon = xm_name

if tizon <= 18.5:
    print('过轻')
elif tizon > 18.5 and tizon <= 25:
    print('正常')
elif tizon > 25 and tizon <= 28:
    print('过重')
elif tizon >28 and tizon <=32:
    print('肥胖')
else:
    print('严重肥胖')




# 练习8：
# 1000元以下商品打9.5折,1000-5000元之间的商品打9折，其他情况打8.5折。
# 请编写程序代码:
# 实现对任意输入一件商品售价，能够输出其优惠价格与最终价格。
# 并实现输出结果为：
# 输入数字  Enter amount: 960
#
# 折扣数 Discount 48.0
#
# 最终支付 Net payable: 912.0
#
jiage = float(input("请输入商品总价："))

if jiage <= 1000:
    print(jiage)
    zhekou = jiage-jiage * 0.95
    print(zhekou)
    zhifu = jiage * 0.95
    print(zhifu)
elif jiage > 1000 and jiage <=5000:
    print(jiage)
    zhekou = jiage-jiage * 0.9
    print(zhekou)
    zhifu = jiage * 0.9
    print(zhifu)
else:
    if jiage > 5000:
        print(jiage)
        zhekou = jiage-jiage * 0.85
        print(zhekou)
        zhifu = jiage * 0.85
        print(zhifu)


# 练习9
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位，请用代码实现
#
#
chengji = 72
xianfen = 85
baifenbi = xianfen/chengji
print('%.1f%%' % (baifenbi * 100))  # 查找显示百分比的代码








练习1
打印单词'interested'中的每一个字母。


练习2
对列表Names = ['Bart', 'Lisa', 'Adam']中的每个名字打印Hello,xxx


练习3
计算1-100内所有偶数的和。


练习4
倒序输出列表[1,2,3,4,5]中的元素

练习5
编写代码，使用 if...elif...else 语句判断输入的一个数字是正数、负数或零.

练习6
根据输入年龄，对其称谓进行归类： 大于18岁，输出 adult，小于18岁，输出teenager。
编写代码，使输出结果为：
your age is 3
teenager

练习7
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻 18.5-25：正常 25-28：过重 28-32：肥胖 高于32：严重肥胖
请用代码实现它,并实现输出结果为：
your bmi is: 26.285714285714285
过重

练习8：
1000元以下商品打9.5折,1000-5000元之间的商品打9折，其他情况打8.5折。
请编写程序代码:
实现对任意输入一件商品售价，能够输出其优惠价格与最终价格。
并实现输出结果为：
Enter amount: 960

Discount 48.0

Net payable: 912.0

练习9
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位，请用代码实现






