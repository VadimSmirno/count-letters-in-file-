import zipfile


def upzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(file_name):
    result = {}
    count = 0
    if file_name.endswith('.zip'):
        upzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    for key, velues in result.items():
        count += int(velues)

    return (result,count)



def print_stats(stats,count_letter):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('Буква', 'Частота'))
    print('+{:-^19}+'.format('+'))
    for i_elem in stats:
        percent = ('{:.5%}').format(int(i_elem[1])/count_letter)
        print('|{: ^9}|{: ^9}|'.format(i_elem[0], percent))
    print('+{:-^19}+'.format('+'))


def sort_by_frequency(stats_dict):
    lst_dict = list(stats_dict.items())
    lst_dict.sort(key=lambda i: i[1])
    return lst_dict


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats1 = sort_by_frequency(stats[0])
print_stats(stats1,stats[1])
