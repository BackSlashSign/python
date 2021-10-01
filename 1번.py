class Bag: 

    def __init__(self): 

        self.items = []  
    def contains(self, e):
        if self.items.count(e) >0:
            return True
        elif self.items.count(e) == 0:
            return False

    def insert(self, e): 
        self.items.append(e)
        return

    def remove(self, e): 
        self.items.remove(e)
        return

    def count(self): 
        return self.items.__len__()
    
    def __str__(self):  
        return format(self.items)


myBag = Bag() 

myBag.insert("휴대폰") 

myBag.insert("지갑") 

myBag.insert("손수건") 

myBag.insert('빗') 

myBag.insert('연필') 

print("가방속 물건: ", myBag) 

 

myBag.insert('빗') 

myBag.remove('손수건') 

myBag.insert('자료 구조 책') 

print("가방속 물건: ", myBag) 

print("가방속 물건 갯수: %d" %myBag.count()) 

print("가방속 지갑 유무: %s" %myBag.contains('지갑')) 

print("가방속 손수건 유무: %s" %myBag.contains('손수건')) 
 



# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("{0}의 공격력 : {1} | 체력 : {2} 입니다.".format(self.name, self.damage, self.hp))
#     def damaged():
#         return
# class AttackUnit(Unit) :
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage
        
#     def Attack(self,location):
#         print("{0} : {1} 시 방향으로 적을 공격합니다.".format(self.name,location))
#         return



# marineUnit = AttackUnit("마린",40,5)
