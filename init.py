# -*- coding: utf-8 -*-
import csv
import os
import time
import sys


def get_summ(month, den, god, usluga):
    """Сумма реестров"""
    return sum([float(open(i, 'r').readlines()[1].lstrip('# ').split(' ')[0]) for i in get_filelist(month, den, god, usluga)])


def get_filelist(month, day, year, service):
    coding = sys.stdin.encoding
    if __name__ == "__main__":
        if month == '':
            month = '05'
        if day == '':
            day = '05'
        if year == '':
            year = '2015'
        service = raw_input('Введите услугу(1 Альт, 2 Мастер, 3 МЖКО):'.decode('UTF-8').encode(coding))
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    dpap = year + '_' + month + '_' + day
    if service == '1':
        reestr_directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'альт'
    elif service == '2':
        reestr_directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'мастер'
    elif service == '3':
        reestr_directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'МЖКО'
    elif service == '0':
        reestr_directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    else:
        reestr_directory = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    if not os.path.exists(reestr_directory):
        return []

    files = os.listdir(reestr_directory)
    files = filter(lambda x: x.endswith('.txt'), files)
    files = [reestr_directory + '/' + fil for fil in files]
    return files


def search_csv(files, search_str):
    lst = []
    for fil in files:
        [lst.append(unicode(", ".join(row), 'cp866')) for row in csv.reader(open(fil, "rb")) if unicode(search_str.upper(), 'utf-8') in unicode(", ".join(row), 'cp866')]
    return lst


def main():
    coding = sys.stdin.encoding
    day = raw_input('Введите нужный день:'.decode('UTF-8').encode(coding))
    month = raw_input('Введите нужный месяц:'.decode('UTF-8').encode(coding))
    year = raw_input('Введите нужный год:'.decode('UTF-8').encode(coding))
    search_str = raw_input('Введите искомую строку:'.decode('UTF-8').encode(coding))
    search_csv(get_filelist(month, day, year, ''), search_str)
    a = raw_input('')
    print a

if __name__ == "__main__":
    while True:
        main()
