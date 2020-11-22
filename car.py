class Car():  
    def __init__(self,brand,type,color,weight,oilcostper100km): #构造方法
        self.brand = brand
        self.type = type
        self.oilcostper100km = oilcostper100km
        self.color = color
        self.weight = weight
      
    def __repr__(self):
        s="In __repr__:\n    <{} object at {:#016x}>\n".format(repr(self.__class__),id(self) )#使用类相关的信息输出类名和实例ID
        s+=super().__repr__() #直接调用object.__repr__方法输出类信息和实例ID
        s+='\n'+repr(self.__dict__)
        return s
  
    # def __str__(self):
    #     return "In __str__:\n    实例属性：{} {}，车身颜色{}、车重{}吨、百公里油耗{}升".\
    #     format(self.brand,self.type,self.color,self.weight,self.oilcostper100km)
if __name__ =='__main__':
    car = Car('雪佛兰','科帕奇','白色',1.8,10)
    print("print_car",car) #查看实例信息，此时会调用__str__方法，但没有重写__str__方法，效果会怎样？
