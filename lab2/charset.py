TABLE1_CHARSET = 'cp437'
TABLE2_CHARSET = 'cp866'
TABLE3_CHARSET = 'cp1251'

OUTPUT_CHARSET = 'utf-8'

with open('charset.txt', 'w', encoding=OUTPUT_CHARSET) as outf:
    for i in range(0, 256):
        bs = bytes([i])
        ch1 = bs.decode(TABLE1_CHARSET)
        ch2 = bs.decode(TABLE2_CHARSET)
        ch3 = bs.decode(TABLE3_CHARSET, "replace")
        print("{0:3d} - {0:08b} - {0:02X} - {1:1s} - {2:1s} - {3:1s}".format(i, ch1, ch2, ch3), file=outf)

