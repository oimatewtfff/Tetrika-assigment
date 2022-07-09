import wikipediaapi
from datetime import datetime

start_time = datetime.now()
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
    if animal.title[0].upper() == 'Б':
        b += 1
    if animal.title[0].upper() == 'В':
        v += 1
    if animal.title[0].upper() == 'Г':
        g += 1
    if animal.title[0].upper() == 'Д':
        d += 1
    if animal.title[0].upper() == 'Е':
        e += 1
    if animal.title[0].upper() == 'Ж':
        j += 1
    if animal.title[0].upper() == 'З':
        z += 1
    if animal.title[0].upper() == 'И':
        i += 1
    if animal.title[0].upper() == 'Й':
        yi += 1
    if animal.title[0].upper() == 'К':
        k += 1
    if animal.title[0].upper() == 'Л':
        l += 1
    if animal.title[0].upper() == 'М':
        m += 1
    if animal.title[0].upper() == 'Н':
        n += 1
    if animal.title[0].upper() == 'О':
        o += 1
    if animal.title[0].upper() == 'П':
        p += 1
    if animal.title[0].upper() == 'Р':
        r += 1
    if animal.title[0].upper() == 'С':
        s += 1
    if animal.title[0].upper() == 'Т':
        t += 1
    if animal.title[0].upper() == 'У':
        u += 1
    if animal.title[0].upper() == 'Ф':
        f += 1
    if animal.title[0].upper() == 'Х':
        h += 1
    if animal.title[0].upper() == 'Ц':
        c += 1
    if animal.title[0].upper() == 'Ч':
        ch += 1
    if animal.title[0].upper() == 'Ш':
        sh += 1
    if animal.title[0].upper() == 'Щ':
        sha += 1
    if animal.title[0].upper() == 'Э':
        ey += 1
    if animal.title[0].upper() == 'Ю':
        y += 1
    if animal.title[0].upper() == 'Я':
        ya += 1

print('А: ' + str(a))
print('Б: ' + str(b))
print('В: ' + str(v))
print('Г: ' + str(g))
print('Д: ' + str(d))
print('Е: ' + str(e))
print('Ж: ' + str(j))
print('З: ' + str(z))
print('И: ' + str(i))
print('Й: ' + str(yi))
print('К: ' + str(k))
print('Л: ' + str(l))
print('М: ' + str(m))
print('Н: ' + str(n))
print('О: ' + str(o))
print('П: ' + str(p))
print('Р: ' + str(r))
print('С: ' + str(s))
print('Т: ' + str(t))
print('У: ' + str(u))
print('Ф: ' + str(f))
print('Х: ' + str(h))
print('Ц: ' + str(c))
print('Ч: ' + str(ch))
print('Ш: ' + str(sh))
print('Щ: ' + str(sha))
print('Э: ' + str(ey))
print('Ю: ' + str(y))
print('Я: ' + str(ya))
print(datetime.now() - start_time)