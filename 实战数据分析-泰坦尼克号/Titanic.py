# 导入库
import pandas as pd
import numpy as np

# 载入数据

td = pd.read_csv('./titanic/train.csv')
print('td:', td.head(3))

# 修改数据集表头
# 方法1
td1 = pd.read_csv('./titanic/train.csv',
                  names=['乘客ID', '是否幸存', '仓位等级', '姓名', '性别', '年龄', '兄弟姐 妹个数', '父母子女个数', '船票信息', '票价', '客舱',
                         '登船港口'], header=0)
print('td1:', td1.head(3))

# 方法2
td.columns = ['乘客ID', '是否幸存', '仓位等级', '姓名', '性别', '年龄', '兄弟姐 妹个数', '父母子女个数', '船票信息', '票价', '客舱',
              '登船港口']
print('td:', td.head(3))

# 查看数据的基本信息
print('td info: ', td.info())

# 前15行数据 和 后15行
print('td head 10', td.head(10))
print('td tail 15', td.tail(15))

# 判断数据是否为空
print('检测数据是否为空：', td.isnull().head())

# 保存数据
# td.to_csv('./titanic/train_chinese.csv')

# 查看DataFrame数据的每列的项
print(td.columns)

# # 将['PassengerId','Name','Age','Ticket']这几个列元素隐藏，只观察其他几个列元素
# td.drop(['PassengerId', 'Name', 'Age', 'Ticket'], axis=1).head(3)
# print(td)

# 以"Age"为筛选条件，显示年龄在10岁以下的乘客信息
print(td[td["年龄"] < 10].head(3))

# 以"Age"为条件，将年龄在10岁以上和50岁以下的乘客信息显示出来，并将这个数据命名为midage
midage = td[(td["年龄"] > 10) & (td["年龄"] < 50)]
print(midage.head(3))

# 将midage的数据中第100行的"Pclass"和"Sex"的数据显示出来
midage = midage.reset_index(drop=True)
print(midage.head(3))

# 使用iloc方法将midage的数据中第100，105，108行的"Pclass"，"Name"和"Sex"的数据显示出来
print(midage.iloc[[100, 105, 108], [2, 3, 4]])

# 对泰坦尼克号数据（trian.csv）按票价和年龄两列进行综合排序（降序排列)
print(td.sort_values(by=['票价', '年龄'], ascending=False).head(3))

# 还是用之前导入的chinese_train.csv如果我们想看看在船上，最大的家族有多少人（‘兄弟姐妹个数’+‘父母子女个数’）
print('家族有多少人:', max(td['兄弟姐 妹个数'] + td['父母子女个数']))

# 看看泰坦尼克号数据集中 票价 这列数据的基本统计数据
print(td['票价'].describe())

# 看泰坦尼克号数据集中 父母子女个数 这列数据的基本统计数据，
print(td['父母子女个数'].describe())
