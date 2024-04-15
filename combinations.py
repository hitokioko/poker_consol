import json

def load_comb():
    global cardTest
    with open('combination_test.json', 'r') as f:
        cardTest = json.load(f)

load_comb()
KEY = 'data'
main_arr_test = []
for i in cardTest[KEY]:
    # print(i)
    for j in i:
        # print(j)
        main_arr_test.append(j)

def xor(str1, str2):
    return bool(str1) != bool(str2)

EXAMPLE_TABLE = main_arr_test[3] #[['pika', 'J'], ['cherv', '3'], ['cherv', '5'], ['pika', '7'], ['pika', 'T'], ['krest', '7'], ['buba', '6']]
# EXAMPLE_TABLE[3][1] = 'J'


# вернет true если в массиве есть одинаковые значения
def para(hand_and_table): # передаем массив из руки и стола
    arr = []
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив цифр
    for ss in range(0,len(arr)): 
        find_val = arr.pop(ss-ss) #т.к из массива удаляеться значение отнимаем кол во итераций
        if find_val in arr: 
            return True
    return False


for tbl in main_arr_test:
    print(para(tbl))
# print(para(EXAMPLE_TABLE))
# print (EXAMPLE_TABLE)

