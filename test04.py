# กรณี 1 print ( มีข้อมูลกลฃฃหลายประเภท )
# วิธี 1 ใช้ ,
print('hello',555,'wow',999,True,'hi',10 + 30 -5,125.745)

# วิธี 2 ใช้ +
print('hello' + '555' + 'wow' + '999' + 'True' + 'hi' + str(10 + 30 -5) + str(125.745))

# วิธ๊ที่ 3 ใช้เมธอด format()
print('hello {} Wow {} {} Hi {} {}'.format(555,999,True,10+25-5,158.785))
# index number
print('{2} {1} '.format('a','b','c','d','e'))

# วิธี 4 ใช้ f-string 
# ข้อมูลที่ไม่ใฃ่ string เชียนใส่ {} ได้เลย
print(f'hello {555} Wow {999} {True} Hi {10+25-5} {158.785}')