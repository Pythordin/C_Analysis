import re
import os
import glob

def extract_functions_and_variables(c_code):
    # 関数の正規表現パターン
    function_pattern = r'(\w+)\s+(\w+)\s*\([^)]*\)\s*\n{\s*'
    # 変数の正規表現パターン
    variable_pattern = r'(\w+)\s+(\w+)(?:\[\s*\w*\s*\])?;\s*'

    functions = re.findall(function_pattern, c_code)
    variables = re.findall(variable_pattern, c_code)

    return functions, variables

def open_c_files(folder_path):
    # フォルダー内のすべてのC言語ファイルのパスを取得
    c_files = glob.glob(os.path.join(folder_path, '*.c'))

    # 各C言語ファイルを開く
    for file_path in c_files:
        with open(file_path, 'r') as file:
            c_code = file.read()
            functions, variables = extract_functions_and_variables(c_code)

            print("Functions:")
            for func_type, func_name in functions:
                print(f"{func_type} {func_name}()")

            print("\nVariables:")
            for var_type, var_name in variables:
                if (var_type != "return" and var_type != "endif"):
                    print(f"{var_type} {var_name}")


if __name__ == "__main__":
    open_c_files("")