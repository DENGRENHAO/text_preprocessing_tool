# Text Preprocessing Tool

## Overview

給定一個來源.csv檔，將Audio_content_Yamnet與Audio_content_User這兩個欄位整理出Audio_class欄位中。

## Prerequisite

```
git clone https://github.com/DENGRENHAO/text_preprocessing_tool.git
```
```
cd .\text_preprocessing_tool\
```
```
pip3 install -r requirements.txt
```

## Usage

查看可用的選項：

```
python3 main.py --help
```

### 範例

```
python3 main.py -i C:\thomas\test\text_preprocessing_tool\linebot_data.csv
```

- 來源檔案`linebot_data.csv`位於 `C:\thomas\test\text_preprocessing_tool\`中，最後會輸出檔案`new_linebot_data.csv`到本資料夾中
