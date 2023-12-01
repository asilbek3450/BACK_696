class Laptop:
    def __init__(self, model, rangi, gpu, cpu, ram, storage):
        self.model = model
        self.color = rangi
        self.gpu = gpu
        self.cpu = cpu
        self.ram = ram
        self.memory = storage

    def get_info(self, model, rangi, gpu, cpu, ram, storage):
        info = (f'Kompyuterning harakteristikasi quyidagicha:\n'
                f'Modeli {self.model}, {self.color} rangda\n'
                f'Video karta: {self.gpu} GB\n'
                f'Processor: {self.cpu}\n'
                f'Memory: {self.ram} GB | SSD {self.memory} GB\n')
        return info


laptop1 = Laptop('HP', 'Silver', 4, 'Intel Core i5', 8, 256)
laptop2 = Laptop('Lenovo', 'Black', 2, 'Intel Core i3', 4, 128)
laptop3 = Laptop('Asus', 'White', 2, 'Intel Core i3', 4, 128)

print(laptop1.get_info(laptop1.model, laptop1.color, laptop1.gpu, laptop1.cpu, laptop1.ram, laptop1.memory))
print(laptop2.get_info(laptop2.model, laptop2.color, laptop2.gpu, laptop2.cpu, laptop2.ram, laptop2.memory))
print(laptop3.get_info(laptop3.model, laptop3.color, laptop3.gpu, laptop3.cpu, laptop3.ram, laptop3.memory))
