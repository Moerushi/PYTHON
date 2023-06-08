# Задание 44

В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random

lst = ['robot'] * 10

lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

data.head()

[Статья про onehot вид](https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing)

[Решение](https://colab.research.google.com/drive/13aZn1XVLjWLTo1hxcC8m32OhhifY15bv#scrollTo=0b-eZNWS5Pnl)