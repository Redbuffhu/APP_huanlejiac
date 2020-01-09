import yaml

# 读取yaml文件
with open("../Data/search_page.yaml", 'r', encoding='UTF-8') as f:

    data = yaml.safe_load(f)
    # data = yaml.full_load(f)
    # data = yaml.unsafe_load(f)
    print(type(data))
    print(data)


#  写入yaml文件
data = {'Search_sj': {
                        'search_test_02': {'expect': {'value': '现代'}, 'value': 'H'},
                        'search_test_01': {'except': [1, 3, 6], 'value': 'H1'}}}


with open('../Data/text.yaml', 'w', encoding='UTF-8') as f:
    # yaml.safe_dump(data, f)  # 未设置编码格式
    yaml.safe_dump(data, f, encoding='UTF-8', allow_unicode=True)
    print('create data successful!')


with open("../Data/text.yaml", 'r', encoding='UTF-8') as f:
    data = yaml.safe_load(f)
    print(data)
