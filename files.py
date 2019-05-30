with open('referat.txt', 'r', encoding='UTF-8') as referat:
    with open('referat2.txt', 'w', encoding='UTF-8') as referat_2:
        content = referat.read()
        print(len(content))
        without_n = content.replace('\n', ' ')
        content_list = without_n.split(' ')
        x = 0
        for words in content_list:
            x = x + 1
        print(x)

        with_emark = without_n.replace('.', '!')
        print(with_emark)

    
        for each_line in with_emark:
            referat_2.write(each_line)