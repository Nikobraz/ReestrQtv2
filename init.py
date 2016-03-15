# -*- coding: utf-8 -*-
import csv
import os
import time
import sys


def timer(f):
    """Таймер функции"""
    coding = sys.stdin.encoding
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f".decode('UTF-8').encode(coding) % (time.time()-t)
        return res
    return tmp


def get_summ(mesyaz, den, god, usluga):
    """Сумма реестров"""
    return sum([float(open(i, 'r').readlines()[1].lstrip('# ').split(' ')[0]) for i in get_filelist(mesyaz, den, god, usluga)])


def get_filelist(mesyaz, den, god, usluga):
    coding = sys.stdin.encoding
    if __name__ == "__main__":
        if mesyaz == '':
            mesyaz = '05'
        if den == '':
            den = '05'
        if god == '':
            god = '2015'
        usluga = raw_input('Введите услугу(1 Альт, 2 Мастер, 3 МЖКО):'.decode('UTF-8').encode(coding))
    if len(den) == 1:
        den = '0' + den
    if len(mesyaz) == 1:
        mesyaz = '0' + mesyaz
    dpap = god + '_' + mesyaz + '_' + den
    if usluga == '1':
        papka = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'альт'
    elif usluga == '2':
        papka = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'мастер'
    elif usluga == '3':
        papka = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap + '/' u'МЖКО'
    elif usluga == '0':
        papka = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    else:
        papka = u'D:/work/_Chelinvestbank/_Из' ur'\u0020' u'банка/Архив' '/' + dpap
    if not os.path.exists(papka):
        return []

    files = os.listdir(papka)
    files = filter(lambda x: x.endswith('.txt'), files)
    files = [papka + '/' + fil for fil in files]
    return files


def search_csv(files, search_str):
    spisok = []
    search_str = unicode(search_str, 'utf-8')
    for fil in files:
#        print fil
        reader = csv.reader(open(fil, "rb"))
        for row in reader:
            row = ", ".join(row)
            row = unicode(row, 'cp866')
            if search_str.upper() in row:
                spisok.append(row)
    return spisok


def main():
    coding = sys.stdin.encoding
    den = raw_input('Введите нужный день:'.decode('UTF-8').encode(coding))
    mesyaz = raw_input('Введите нужный месяц:'.decode('UTF-8').encode(coding))
    god = raw_input('Введите нужный год:'.decode('UTF-8').encode(coding))
    search_str = raw_input('Введите искомую строку:'.decode('UTF-8').encode(coding))
    search_csv(get_filelist(mesyaz, den, god, ''), search_str)
    a = raw_input('')
    print a

if __name__ == "__main__":
    while True:
        main()
