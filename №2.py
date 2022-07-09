import wikipediaapi
from datetime import datetime

wiki_wiki = wikipediaapi.Wikipedia('ru')

animals = wiki_wiki.page('Категория:Животные по алфавиту')

a = 0
b = 0
v = 0
g = 0
d = 0
e = 0
j = 0
z = 0
i = 0
yi = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
r = 0
s = 0
t = 0
u = 0
f = 0
h = 0
c = 0
ch = 0
sh = 0
sha = 0
ey = 0
y = 0
ya = 0
for animal in animals.categorymembers.values():
    if animal.title[0].upper() == 'А':
        a += 1
    elif animal.title[0].upper() == 'Б':
        b += 1
    elif animal.title[0].upper() == 'В':
        v += 1
    elif animal.title[0].upper() == 'Г':
        g += 1
    elif animal.title[0].upper() == 'Д':
        d += 1
    elif animal.title[0].upper() == 'Е':
        e += 1
    elif animal.title[0].upper() == 'Ж':
        j += 1
    elif animal.title[0].upper() == 'З':
        z += 1
    elif animal.title[0].upper() == 'И':
        i += 1
    elif animal.title[0].upper() == 'Й':
        yi += 1
    elif animal.title[0].upper() == 'К':
        k += 1
    elif animal.title[0].upper() == 'Л':
        l += 1
    elif animal.title[0].upper() == 'М':
        m += 1
    elif animal.title[0].upper() == 'Н':
        n += 1
    elif animal.title[0].upper() == 'О':
        o += 1
    elif animal.title[0].upper() == 'П':
        p += 1
    elif animal.title[0].upper() == 'Р':
        r += 1
    elif animal.title[0].upper() == 'С':
        s += 1
    elif animal.title[0].upper() == 'Т':
        t += 1
    elif animal.title[0].upper() == 'У':
        u += 1
    elif animal.title[0].upper() == 'Ф':
        f += 1
    elif animal.title[0].upper() == 'Х':
        h += 1
    elif animal.title[0].upper() == 'Ц':
        c += 1
    elif animal.title[0].upper() == 'Ч':
        ch += 1
    elif animal.title[0].upper() == 'Ш':
        sh += 1
    elif animal.title[0].upper() == 'Щ':
        sha += 1
    elif animal.title[0].upper() == 'Э':
        ey += 1
    elif animal.title[0].upper() == 'Ю':
        y += 1
    elif animal.title[0].upper() == 'Я':
        ya += 1

print('А: ' + str(a) + '\n' + 'Б: ' + str(b) + '\n' + 'В: ' + str(v) + '\n' + 'Г: ' + str(g) + '\n' + 'Д: ' + str(d) +
      '\n' + 'Е: ' + str(e) + '\n' + 'Ж: ' + str(j) + '\n' + 'З: ' + str(z) + '\n' + 'И: ' + str(i) + '\n' + 'Й: ' +
      str(yi) + '\n' + 'К: ' + str(k) + '\n' + 'Л: ' + str(l) + '\n' + 'М: ' + str(m) + '\n' + 'Н: ' + str(n) + '\n' +
      'О: ' + str(o) + '\n' + 'П: ' + str(p) + '\n' + 'Р: ' + str(r) + '\n' + 'С: ' + str(s) + '\n' + 'Т: ' + str(t) +
      '\n' + 'У: ' + str(u) + '\n' + 'Ф: ' + str(f) + '\n' + 'Х: ' + str(h) + '\n' + 'Ц: ' + str(c) + '\n' + 'Ч: ' +
      str(ch) + '\n' + 'Ш: ' + str(sh) + '\n' + 'Щ: ' + str(sha) + '\n' + 'Э: ' + str(ey) + '\n' + 'Ю: ' + str(y) +
      '\n' + 'Я: ' + str(ya))
