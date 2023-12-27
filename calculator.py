def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("ゼロで割ることはできません")
    return x / y

def calculator():
    print("プログラムを開始します")
    while True:
        try:
            calculate_first = input("計算しますか？（はい/いいえ）：")
            
            if calculate_first.lower() == 'はい':
                print("それでは始めます")
    
                while True:
                    first = float(input("最初の数字を入力してください："))
                    operator = input("演算子を選択してください（+, -, *, /）：")
                    end = float(input("最後の数字を入力してください："))

                    if operator not in ['+', '-', '*', '/']:
                        print("無効な演算子です")
                        continue

                    if operator == '+':
                        result = add(first, end)
                    elif operator == '-':
                        result = subtract(first, end)
                    elif operator == '*':
                        result = multiply(first, end)
                    elif operator == '/':
                        result = divide(first, end)

                    print("結果は {}".format(result))

                    another_calculation = input("別の計算を行いますか？（はい/いいえ）：")
                    if another_calculation.lower() != 'はい':
                        break

                print("さようなら")
                break

            else:
                print("さようなら")
                break

        except ValueError:
            print("有効な数字を入力してください。")
        except Exception as e:
            print("エラーが発生しました:", str(e))
            continue

if __name__ == "__main__":
    calculator()
