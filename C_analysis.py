import re
import os
import glob

import re

def extract_functions_and_variables(c_code, filePath):
    # 関数の正規表現パターン
    function_pattern = r'\b(\w+\s*\*?\s*\w+)\s*\([^)]*\)\s*\n{'

    # 変数の正規表現パターン
    variable_pattern = r'(\w+)\s+(\w+)(?:\[\s*\w*\s*\])?(?:\s*=\s*.+)?;\s*'

    functions = []
    variables = []

    # 行数を保存するための変数
    matches = re.finditer(function_pattern, c_code)

    # 関数のマッチングと行数の保存
    for match in matches:
        start = match.start()
        line_number = c_code.count('\n', 0, start) + 1 
        functions.append(match[1] + "\": \"" + filePath[45:]) # 関数内に含まれる改行の数を加算

    # 変数のマッチングと行数の保存
    for match in re.finditer(variable_pattern, c_code):
        if (match[1] != "return" and match[1] != "endif" and match[1] != "DEBUG" and match[1] != "while" and match[1] != "else" and match[1] != "goto"):
            start = match.start()
            line_number = c_code.count('\n', 0, start) + 1
            variables.append(match[1] + " " + match[2] + " " + str(line_number))  # 変数宣言に含まれる改行の数を加算

    return functions, variables


def open_c_files(folder_path):
    # フォルダー内のすべてのC言語ファイルのパスを取得
    c_files = glob.glob(os.path.join(folder_path, '*.c'))


    # 各C言語ファイルを開く
    for file_path in c_files:
        with open(file_path, 'r') as file:
            #print(file_path)
            c_code = file.read()
            functions, variables = extract_functions_and_variables(c_code, file_path)

            #print("Functions:")
            for func_name in functions:
                a = func_name.split()
                print(f"\"{a[1]}{a[2]}\"", end=",\n")

            #print("\nVariables:")
            for var_type  in variables:
                if (var_type != "return" and var_type != "endif" and var_type != "DEBUG"):
                    #print(f"\"{var_type}\"")
                    pass
            #print()


if __name__ == "__main__":
    open_c_files("/home/iot/ドキュメント/Mirai-Source-Code/mirai/bot/")