#简单的价格运算
the_numbuer_shop=eval(input("输入你想购买的数量"))
the_cost=eval(input("请输入每个商品的价格"))
totle_1=the_cost*the_numbuer_shop
shui=0.05
totle_2=totle_1*shui
totle_3=totle_2+totle_1
print("商品总价：",totle_1)
print("税收：",totle_2)
print(" 实际价格：",totle_3)
