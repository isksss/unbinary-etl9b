# import
import argparse

# arguments
def args_parse():
    """
    コマンドライン引数の解析
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, 
                        help='unzipするデータを指定してください。 ex) 9b')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = args_parse() # コマンドライン引数の解析
    pass
