year = int(input("당신의 출생연도는 무엇입니까?\n"))
value = year % 12

def animal(key):
    animal = {0:"원숭이띠",1:"닭띠",2:"개띠",3:"돼지띠",
              4:"쥐띠",5:"소띠",6:"호랑이띠",7:"토끼띠",
              8:"용띠",9:"뱀띠",10:"말띠",11:"양띠"}.get(key, "알 수 없는 띠")
    print(f'당신은 {animal} 입니다')

animal(value)