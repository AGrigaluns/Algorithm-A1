import png

s = ['01010101',
     '01010101',
     '01010111',
     '01010101',
     '01010101',
     '01110101']

s = [[int(c) for c in row * 50] for row in s * 50]

palette=[(0x00,0x00,0x00), (0x23,0x64,0x42)]
w = png.Writer(len(s[0]), len(s), palette=palette, bitdepth=8)
f = open('logo2.png', 'wb')
w.write(f, s)


