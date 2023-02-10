OP airdrop2 查询脚本使用（灵感来自gm365老师）

1.读取 address.txt 文件中的每一项，作为 address
2.读取 score.csv 文件，第一列为 address, 第二列为 score 
3.遍历 address.txt 中每一项，查询 score.csv 中对应地址的 score

score.csv 空投文件已经给出，需要自己添加一个 address.txt，然后运行 op_airdrop2_query.py，results.csv就是我们需要文件
