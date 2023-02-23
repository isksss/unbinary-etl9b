# unbinary-etl9b

## 使い方
1. `data`フォルダにETL9Bのzipファイルを置く。
2. `python main.py --target 9b`を実行する。

distフォルダに画像が出力されます。　　

## 環境
|||
|:-:|:--|
|python|3.11|

## TODO
### 開発段階
- コマンドライン引数の解析
- 関数
  - zip解凍
  - 指定ファイルのアンバイナリ
  - 出力

### 実装予定
- 9B以外にも対応する ex) 9G, 8G...