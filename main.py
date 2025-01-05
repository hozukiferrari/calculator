#1 add, 2 subtract, 3 multiply, 4 divide
class calculator(object):
    def __init__(self):
        super(calculator, self).__init__()
        self.current_result = 0
        self.final_result = 0
        self.first_value = int(input("Masukkan nilai pertama : "))
        self.second_value = int(input("Masukkan nilai kedua : "))
        self.current_operator = int(input("Masukkan jenis operator!\n1)Tambah\n2)Kurang\n3)Kali\n4)Bagi\nPilih salah satu : "))       
        self.operasi(self.first_value, self.second_value)
        self.progress()
    def progress(self):
        while True:
            self.confirm = str(input("Apakah masih mau melanjutkan operasi ? Y/N : "))
            if self.confirm.lower() == "y":
                print(f"nilai pertama anda ialah hasil sebelumnya yaitu : {self.current_result}")
                self.second_value = input("Masukkan nilai kedua : ")
                self.current_operator = int(input("Masukkan jenis operator!\n1)Tambah\n2)Kurang\n3)Kali\n4)Bagi\nPilih salah satu : "))
                self.operasi(self.current_result, self.second_value)
            elif self.confirm.lower() == "n":
                self.final_result = self.current_result
                break
            else:
                print("Terjadi kesalahan")
                self.final_result = self.current_result
                break
    def operasi(self,val1,val2):
        if self.current_operator == 1:
            self.current_result = self.add(val1, val2)
        if self.current_operator == 2:
            self.current_result = self.substract(val1, val2)
        if self.current_operator == 3:
            self.current_result = self.multiply(val1,val2)
        if self.current_operator == 4:
            self.current_result = self.divide(val1, val2)
    def add(self, value1, value2):
        return int(value1 + value2)
    def subtract(self, value1, value2):
        return int(value1 - value2)
    def multiply(self, value1, value2):
        return int(value1 * value2)
    def divide(self, value1, value2):
        return float(int(value1) / int(value2))
def main():
    calc = calculator()
    print(f"hasil : {calc.final_result}")
if __name__ == '__main__':
    main()