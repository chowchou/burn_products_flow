# add = 'C:/Users/lenovo/Desktop/cpyctrl_V1_7-sta-plc-flash-0xAA540AC8.bin'
#
# with open(add,'rb') as f:
#     dblst = f.read()
# import binascii
# crc32 = binascii.crc32(dblst)
# def check_num(num):
#     check_id = "%.2x" % (sum([int(sn, 16) for sn in num.split(" ")]) % 256)
#     return check_id
# avc = '03 02 00 00 00 01 22 22 22 00 00 00'
# sa = check_num(avc)
# print(sa)
#
#
#
# def add_length(num):
#     lens = int(len(num) / 2)
#     length  = hex(lens).upper()
#     length = '0' + length[2:]
#     return length
# f2 = lambda b: "%.2X" % (int.from_bytes(b,"little"))
# for i in range(int(len(dblst)/1024)+1):
#     # lists = []
#     res = dblst[i*1024:(i+1)*1024] #取第N个1KB
#     # print(type(res))
#     res_1 = res.hex().upper()
#     # lens = int(len(res_1)/2)#计算文件长度
#     nm = add_length(res_1)#计算文件长度,文件长度补0
#     print(nm)
#     cs = nm + res_1
#     # print(cs)
#     import re
#     # text_list = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", cs)
#     text_list = re.findall(".{2}", cs)
#     new_text = " ".join(text_list)
#     # print(new_text)
#     jisuan ='03 0D 00 00 00 04 ' + new_text #补充命令帧
#     # print(jisuan)
#     check_id = "%.2x" % (sum([int(sn, 16) for sn in jisuan.split(" ")]) % 256) #计算校验位
#
#     addc = jisuan + str(check_id) #命令 + 校验位
#     add_len = addc.replace(" ", "").upper()
#     nm1 = add_length(add_len)#计算命令长度补0
#     all_order = 'ED' + nm1 + add_len + 'EE' #整合命令帧
#     # print(all_order)





# id_mod = ''
# check_id = "%.x" % (sum([int(sn, 16) for sn in id_mod.split(" ")]) % 256)

# a = [dblst[i*1024:(i+1)*1024] for i in range(int(len(dblst)/1024)+1)]
# print(type(a[-1]))
#
# print(len(a))

# f2 = lambda b: "%.2X" % (int.from_bytes(b,"little"))
# def f1(ipt):
#     try:
#         return f2(ipt)
#     except Exception as e:
#         print(e)
#         print("#33")
#         print(type(a))
#         print(ipt)
#         print("#34")
#         return  ""
#
# ks1 = [[f1(j[i:i+1]) for i in range(len(j))] for j in a]
#
# print(ks1)

# a= 'ED 04 09 03 0D 00 00 00 04 04 00 64 20 74 78 5F 69 6E 74 65 72 76 61 6C 20 0D 0A 5B 65 6E 61 62 6C 65 5D 3A 20 65 6E 61 62 6C 65 3B 20 30 3A 20 64 69 73 61 62 6C 65 20 74 65 73 74 62 65 6E 63 68 3B 20 0D 0A 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 31 3A 20 65 6E 61 62 6C 65 20 74 65 73 74 62 65 6E 63 68 28 6C 65 67 61 63 79 29 0D 0A 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 32 3A 20 65 6E 61 62 6C 65 20 63 6F 6D 6D 20 74 65 73 74 20 6D 6F 64 65 0D 0A 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 33 3A 20 65 6E 61 62 6C 65 20 74 65 73 74 62 65 6E 63 68 28 6C 65 67 61 63 79 29 2C 64 6F 6E 27 74 20 75 70 64 61 74 65 20 70 68 79 20 73 74 61 74 69 63 20 70 61 72 61 6D 0D 0A 5B 77 6F 72 6B 5F 62 61 6E 64 5D 3A 20 77 6F 72 6B 20 62 61 6E 64 2C 20 30 3A 20 62 61 6E 64 30 2C 20 31 3A 20 62 61 6E 64 31 0D 0A 5B 6D 70 64 75 5F 74 79 70 65 5D 3A 20 6D 70 64 75 20 74 79 70 65 2C 20 30 3A 20 62 65 61 63 6F 6E 2C 20 31 3A 20 73 6F 66 2C 20 32 3A 73 61 63 6B 2C 20 33 3A 20 6E 63 66 20 0D 0A 5B 70 62 5F 6E 75 6D 5D 3A 20 70 62 5F 6E 75 6D 20 66 6F 72 20 73 6F 66 2C 20 72 61 6E 67 65 3A 20 30 7E 34 20 0D 0A 5B 74 6D 69 5F 62 61 73 69 63 5D 3A 20 74 6D 69 20 62 61 73 69 63 20 6D 6F 64 65 2C 20 72 61 6E 67 65 3A 20 30 7E 31 34 0D 0A 5B 74 6D 69 5F 65 78 74 5D 3A 20 74 6D 69 20 65 78 74 20 6D 6F 64 65 2C 20 31 7E 36 2C 31 30 7E 31 34 20 0D 0A 5B 70 68 61 73 65 5D 3A 20 70 68 61 73 65 2C 20 72 61 6E 67 65 3A 20 31 7E 33 20 0D 0A 5B 72 65 70 6F 72 74 5F 70 65 72 69 6F 64 5D 3A 20 72 65 70 6F 72 74 20 70 65 72 69 6F 64 2C 20 72 61 6E 67 65 3A 20 31 7E 31 30 32 34 0D 0A 5B 74 78 5F 69 6E 74 65 72 76 61 6C 5D 3A 20 74 78 20 69 6E 74 65 72 76 61 6C 2C 20 75 6E 69 74 20 69 73 20 6D 69 6C 6C 69 73 65 63 6F 6E 64 3B 20 72 61 6E 67 65 3A 31 7E 31 30 30 00 70 74 62 64 00 70 68 79 20 74 65 73 74 62 65 6E 63 68 20 64 61 74 61 20 73 65 6E 64 20 63 6F 6D 6D 61 6E 64 2E 20 0D 0A 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 70 74 62 64 20 74 79 70 65 20 70 31 20 70 32 20 70 33 20 70 34 20 70 35 20 70 36 20 70 37 20 70 38 20 0D 0A 5B 74 79 70 65 5D 3A 20 64 61 74 61 20 74 79 70 65 3B 20 30 3A 20 61 70 6C 20 63 6F 6D 6D 20 74 65 73 74 20 66 72 61 6D 65 3B 20 0D 0A 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 31 3A 20 6D 70 64 75 20 66 72 61 6D 65 20 0D 0A 74 79 70 65 3D 30 3A 0D 0A 5B 70 31 5D 3A 20 74 65 73 74 20 6D 6F 64 65 2C 20 31 7E 37 20 0D 0A 5B 70 32 5D 3A 20 70 61 72 61 6D 20 0D 0A 5B 70 33 5D 3A 20 74 6D 69 20 62 61 73 69 63 20 6D 6F 64 65 2C 20 72 61 6E 67 65 3A 20 30 7E 31 34 20 0D 0A 5B 70 34 5D 3A 20 6E 75 6D 2C 20 74 72 61 6E 73 6D 69 73 73 69 6F 6E 20 74 69 6D 65 73 20 0D 0A 5B 70 35 5D 3A 20 74 78 20 69 6E 74 65 72 76 61 6C 2C 20 75 6E 69 74 20 69 73 20 6D 69 6C 6C 69 73 65 63 6F 6E 64 3B 20 72 61 6E 67 65 3A 31 7E 31 30 30 20 0D 0A 5B 70 36 5D 3A 20 77 6F 72 6B 20 62 61 6E 64 2C 20 30 3A 20 62 61 6E 64 30 2C 20 31 3A 20 62 61 6E 64 31 20 0D 0A 5B 70 37 5D 3A 20 74 6F 6E 65 6D 61 73 6B 2C 20 30 3A 20 74 6F 6E 65 6D 61 73 6B 30 2C 20 31 3A 20 74 6F 6E 65 6D 61 73 6B 31 2C 20 2D 31 3A 20 69 6E 76 61 6C 69 64 20 20 5A'
#
# b = '70 FA 9B 52 2A BF 0D ED CD 97 7E 58 B0 26 1F 6C 90 6D 7F 20 4C 43 B9 E8 39 79 7E 5F 3B B8 9A 07 1D F4 B5 43 A9 A1 90 01 35 10 6D B8 A1 E8 CD E8 5A B1 10 3A 74 B3 43 B2 10 BF A6 9E DC 51 7B A0 D3 64 07 E2 9B 67 28 89 EA E2 A6 7C 7B CB 5F A6 E5 C6 C3 B3 68 13 B0 BA 3D 35 14 BC 7F 2F D5 C5 61 DB 31 F5 6A 12 98 85 6A 98 F7 48 D3 3E 40 02 68 D4 83 C0 71 20 85 47 CA CD 20 5B 52 76 A0 B9 DC 0F BC 67 25 CD 61 0B 71 7A 84 B0 81 70 0B C2 94 50 FA A7 51 FA E5 E8 E7 07 85 B6 BF 46 87 FB 4B F9 4C 7F E1 1F B2 B9 51 6A 45 A0 0E B7 6F B9 27 49 FB CB D0 9B 92 50 B6 2D AC B8 B7 9F A1 91 A1 A9 DC AC A9 AB 78 98 D8 C9 60 67 E1 29 CB 54 81 2D 79 56 81 4E 6C 15 E0 AF CB CB 42 65 CA ED D5 4F F1 46 F0 97 8F 25 10 42 65 48 13 4E 82 D0 25 7D EB 28 B8 02 00 00 00 00 00 00 00 00 00 00 67 45 23 01 57 34 12 46 23 71 45 23 01 57 23 01 46 72 35 71 56 23 41 02 57 23 70 56 34 12 60 45 12 67 35 70 46 31 24 35 73 06 36 50 61 37 41 32 06 12 46 44 41 56 07 32 31 61 07 60 11 73 07 73 15 24 04 54 53 15 15 55 42 22 13 73 30 17 62 40 61 33 02 31 16 67 31 77 14 60 22 53 61 54 07 06 14 44 01 24 41 65 55 25 67 71 35 46 27 54 76 37 62 71 47 60 62 76 51 72 77 50 06 75 75 74 52 44 21 03 40 40 54 72 54 76 10 13 57 70 56 21 47 26 26 33 10 17 72 41 75 32 16 41 62 60 45 71 61 77 37 03 46 71 35 24 15 30 64 73 36 74 71 22 50 65 67 04 61 51 57 17 67 25 54 12 45 60 07 05 50 01 46 51 46 66 26 72 03 56 61 70 10 50 25 56 24 57 71 31 36 23 43 32 26 65 50 01 33 53 31 60 61 13 76 16 04 44 65 23 26 63 72 11 54 43 72 52 33 07 57 26 04 11 74 76 36 06 77 65 56 40 46 17 24 14 C1 65 59 B2 00 00 00 00 00 00 01 01 01 02 02 02 03 03 03 04 04 04 05 05 05 06 06 06 07 07 07 08 08 08 09 09 09 0A 0A 0A 0B 0B 0B 0C 0C 0C 0D 0D 0D 0E 0E 0E 0F 0F 0F 10 10 10 11 11 11 12 12 12 13 13 13 14 14 14 15 15 15 16 16 16 17 17 17 18 18 18 19 19 19 1A 1A 1A 1B 1B 1B 1C 1C 1C 1D 1D 1D 1E 1E 1E 1F 1F 1F 20 20 20 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 42 AC DF D0 FF FF FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FE FF FF FF FF FF FF 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F8 FF FF F3 5F 83 E4 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 3F 00 00 00 00 00 00 00 00 00 80 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 28 05 57 83 FF FF FF FF FF FF FF FF FF FF FF FF 0F 00 00 00 00 00 00 00 00 00 00 00 00 00 80 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF AC 4A 08 72 FF FF FF FF 00 00 00 E0 FF FF FF FF FF FF 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF B3 02 17 17 FF FF FF FF FF FF FF FF FF FF FF FF 3F 00 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF AB 65 78 2B 4B 0F 97 C1 7E 1C D3 D0 7E 2E 09 C5 E2 21 F4 CE C1 2E 62 B4 FF 2B 6A 4E C3 D4 FF 1F 24 BC 20 F4 F1 92 6E 3A'
# # print(len(b.split(' ')))
# s = len(b.split(' '))
# # s = hex(s)
# # print("%02X" % s)
# c = '04 09 03 0D 00 00 00 04 04 00 70 FA 9B 52 2A BF 0D ED CD 97 7E 58 B0 26 1F 6C 90 6D 7F 20 4C 43 B9 E8 39 79 7E 5F 3B B8 9A 07 1D F4 B5 43 A9 A1 90 01 35 10 6D B8 A1 E8 CD E8 5A B1 10 3A 74 B3 43 B2 10 BF A6 9E DC 51 7B A0 D3 64 07 E2 9B 67 28 89 EA E2 A6 7C 7B CB 5F A6 E5 C6 C3 B3 68 13 B0 BA 3D 35 14 BC 7F 2F D5 C5 61 DB 31 F5 6A 12 98 85 6A 98 F7 48 D3 3E 40 02 68 D4 83 C0 71 20 85 47 CA CD 20 5B 52 76 A0 B9 DC 0F BC 67 25 CD 61 0B 71 7A 84 B0 81 70 0B C2 94 50 FA A7 51 FA E5 E8 E7 07 85 B6 BF 46 87 FB 4B F9 4C 7F E1 1F B2 B9 51 6A 45 A0 0E B7 6F B9 27 49 FB CB D0 9B 92 50 B6 2D AC B8 B7 9F A1 91 A1 A9 DC AC A9 AB 78 98 D8 C9 60 67 E1 29 CB 54 81 2D 79 56 81 4E 6C 15 E0 AF CB CB 42 65 CA ED D5 4F F1 46 F0 97 8F 25 10 42 65 48 13 4E 82 D0 25 7D EB 28 B8 02 00 00 00 00 00 00 00 00 00 00 67 45 23 01 57 34 12 46 23 71 45 23 01 57 23 01 46 72 35 71 56 23 41 02 57 23 70 56 34 12 60 45 12 67 35 70 46 31 24 35 73 06 36 50 61 37 41 32 06 12 46 44 41 56 07 32 31 61 07 60 11 73 07 73 15 24 04 54 53 15 15 55 42 22 13 73 30 17 62 40 61 33 02 31 16 67 31 77 14 60 22 53 61 54 07 06 14 44 01 24 41 65 55 25 67 71 35 46 27 54 76 37 62 71 47 60 62 76 51 72 77 50 06 75 75 74 52 44 21 03 40 40 54 72 54 76 10 13 57 70 56 21 47 26 26 33 10 17 72 41 75 32 16 41 62 60 45 71 61 77 37 03 46 71 35 24 15 30 64 73 36 74 71 22 50 65 67 04 61 51 57 17 67 25 54 12 45 60 07 05 50 01 46 51 46 66 26 72 03 56 61 70 10 50 25 56 24 57 71 31 36 23 43 32 26 65 50 01 33 53 31 60 61 13 76 16 04 44 65 23 26 63 72 11 54 43 72 52 33 07 57 26 04 11 74 76 36 06 77 65 56 40 46 17 24 14 C1 65 59 B2 00 00 00 00 00 00 01 01 01 02 02 02 03 03 03 04 04 04 05 05 05 06 06 06 07 07 07 08 08 08 09 09 09 0A 0A 0A 0B 0B 0B 0C 0C 0C 0D 0D 0D 0E 0E 0E 0F 0F 0F 10 10 10 11 11 11 12 12 12 13 13 13 14 14 14 15 15 15 16 16 16 17 17 17 18 18 18 19 19 19 1A 1A 1A 1B 1B 1B 1C 1C 1C 1D 1D 1D 1E 1E 1E 1F 1F 1F 20 20 20 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 42 AC DF D0 FF FF FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FE FF FF FF FF FF FF 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F8 FF FF F3 5F 83 E4 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 3F 00 00 00 00 00 00 00 00 00 80 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 28 05 57 83 FF FF FF FF FF FF FF FF FF FF FF FF 0F 00 00 00 00 00 00 00 00 00 00 00 00 00 80 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF AC 4A 08 72 FF FF FF FF 00 00 00 E0 FF FF FF FF FF FF 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF B3 02 17 17 FF FF FF FF FF FF FF FF FF FF FF FF 3F 00 00 FE FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF AB 65 78 2B 4B 0F 97 C1 7E 1C D3 D0 7E 2E 09 C5 E2 21 F4 CE C1 2E 62 B4 FF 2B 6A 4E C3 D4 FF 1F 24 BC 20 F4 F1 92 6E 3A B6'
# # print(len(c.split(' ')))
# s = len(c.split(' '))
# s = hex(s)
# print(s)

#
# s = 'AAVBCDFGDDDSSA112D6'
#
# b = 'A112D2'
#
# if b in s:
#     print('True')
# else:
#     print('False')
import configparser
# import re
#
# dicts = {}
# read_ini = configparser.ConfigParser()
# read_ini.read('config.ini')
# a = read_ini.items('dev')
# print(len(a))
# for i in range(len(a)):
#     # print(a[i][0])
#     # print(a[i][1])
#     dicts[a[i][0]] = a[i][1]
# print(dicts)
# ssd = 0
# sname = 'dev_' + str(ssd)
# dev_value = dicts.get(sname)
# sup_over = re.findall(".{2}", dev_value)
# sup_over = " ".join(sup_over)
# print(sup_over)
# prefix = 'ED 00 0D '
# devId_len = '03 02 00 00 00 01 '+sup_over
# check_id = "%.2x" % (sum([int(sn, 16) for sn in devId_len.split(" ")]) % 256)
# print(check_id)
# last_devid_order = prefix + devId_len + check_id + 'EE'
# print(last_devid_order)
import re

import public_var
read_ini = configparser.ConfigParser()
read_ini.read('config.ini')
public_var.com_port = read_ini.get('test option', 'com')
public_var.bps = read_ini.get('test option','bps')
public_var.burn_flag = int(read_ini.get('test option','burn_flag'))
public_var.config_dict = {'0':read_ini.get('test station','order_id'),
                          '1':read_ini.get('test station', 'min_txd'),
                          '2':read_ini.get('test station', 'max_txd'),
                          '3':read_ini.get('test station', 'min_sta'),
                          '4':read_ini.get('test station', 'max_sta'),
                          '5':read_ini.get('test station', 'min_cap'),
                          '6':read_ini.get('test station', 'max_cap'),
                          '7': read_ini.get('test station', 'min_1.2v'),
                          '8': read_ini.get('test station', 'max_1.2v'),
                          '9': read_ini.get('test station', 'min_3.3v'),
                          '10': read_ini.get('test station', 'max_3.3v'),
                          '11': read_ini.get('test station', 'min_12vboost'),
                          '12': read_ini.get('test station', 'max_12vboost'),
                          '13': read_ini.get('test station', 'min_damping'),
                          '14': read_ini.get('test station', 'max_damping'),
                          '15': read_ini.get('test station', 'min_fre_offset'),
                          '16': read_ini.get('test station', 'max_fre_offset'),
                          '17': read_ini.get('test station', 'min_set_static'),
                          '18': read_ini.get('test station', 'max_set_static'),
                          '19': read_ini.get('test station', 'min_set_dynamic'),
                          '20': read_ini.get('test station', 'max_set_dynamic'),
                          '21': read_ini.get('test station', 'soft_version'),
                          '22': read_ini.get('test station', 'version'),}


# option_Test = read_ini.get('test option','option_list')
# option_Test = option_Test.split(',')
# print(option_Test)
# list1 = {'0':False,'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False}
# for i in range(len(option_Test)):
#     res = int(option_Test[i])
#     s = str(i)
#     list1[s] = res
# print(list1)
a = '-55'
print(int(a))
print('**'*30)
f2 = lambda d:"%.X"%(int(65536 - abs(d))) if (d < 0) else "%.4X"%(d)
# print(f1(-55),f1(-45),f1(-40),f1(10))

def count_nums(data):
    data = data.split(',')
    res_list = []
    for i in data:
        res = "%.2X"%(int(i))
        res_list.append(res)
    return ''.join(res_list)
def count_2nums(data):
    data = data.split(',')
    res_list = []
    f2 = lambda d: "%.4X" % (int(65536 - abs(d))) if (d < 0) else "%.4X" % (d)
    for i in data:
        res = f2(int(i))
        res_list.append(res)
    return ''.join(res_list)
rx_snr = count_nums(read_ini.get('communication','rx_snr_min_max'))
rx_flatness = count_nums(read_ini.get('communication','rx_flatness_min_max'))
rx_rssi = count_2nums(read_ini.get('communication','rx_rssi_min_max'))
com_succ = count_nums(read_ini.get('communication','com_succ_min_max'))
tx_snr = count_nums(read_ini.get('communication','tx_snr_min_max'))
tx_flatness = count_nums(read_ini.get('communication','tx_flatness_min_max'))
tx_rssi = count_2nums(read_ini.get('communication','tx_rssi_min_max'))
end_order = rx_snr + rx_flatness + rx_rssi + com_succ + tx_snr + tx_flatness + tx_rssi


# f1 = lambda d:"%.2X"%(int(256 - abs(d))) if (d < 0) else "%.2X"%(d)
#
# rx_snr_min = read_ini.get('communication','rx_snr_min')
# # print(hex(int(rx_snr_min)))
# last_rx_snr_min = f1(int(rx_snr_min))
# # print(s.upper())
# rx_snr_max = read_ini.get('communication','rx_snr_max')
# last_rx_snr_max = f1(int(rx_snr_max))
# # print(s.upper())
# rx_rssi_min = read_ini.get('communication','rx_rssi_min')
# # print(rx_rssi_min)
# last_rx_rssi_min = f2(int(rx_rssi_min))
# # print(s.upper())
# rx_rssi_max = read_ini.get('communication','rx_rssi_max')
# last_rx_rssi_max = f2(int(rx_rssi_max))
# # print(s.upper())
# com_succ_min = read_ini.get('communication','com_succ_min')
# last_com_succ_min = f1(int(com_succ_min))
# # print(s.upper())
# com_succ_max = read_ini.get('communication','com_succ_max')
# last_com_succ_max = f1(int(com_succ_max))
# # print(s.upper())
# tx_snr_min = read_ini.get('communication','tx_snr_min')
# last_tx_snr_min = f1(int(tx_snr_min))
# tx_snr_max = read_ini.get('communication','tx_snr_max')
# last_tx_snr_max = f1(int(tx_snr_max))
# tx_rssi_min = read_ini.get('communication','tx_rssi_min')
# last_tx_rssi_min = f2(int(tx_rssi_min))
# tx_rssi_max = read_ini.get('communication','tx_rssi_max')
# last_tx_rssi_max = f2(int(tx_rssi_max))
# rx_flatness_min_max = read_ini.get('communication','rx_flatness_min_max')
# res = rx_flatness_min_max.split(',')
# new_res = []
# for i in res:
#     s = "%.2x" %int(i)
#     # print(s)
#     new_res.append(s)
# last_rx_flatness = ''.join(new_res)
#
# tx_flatness_min_max = read_ini.get('communication','tx_flatness_min_max')
# res = tx_flatness_min_max.split(',')
# new_res = []
# for i in res:
#     s = "%.2x" %int(i)
#     # print(s)
#     new_res.append(s)
# last_tx_flatness = ''.join(new_res)
#
# order_list = [last_rx_snr_min,last_rx_snr_max,last_rx_flatness,last_rx_rssi_min,last_rx_rssi_max,last_com_succ_min,last_com_succ_max,last_tx_snr_min,last_tx_snr_max]
#
# print(order_list)






# arguments = []
# config_value = []
# config_key = [5, 6, 11, 12,]
# for i in config_key:
#     num = public_var.config_dict.get(str(i))
#     config_value.append(num)
# for i in config_value:
#     if '.' not in i:
#         i = i + '.'
#     # 整数
#     num_i = i[0:i.rfind('.')].rjust(2, '0')
#     arguments.append(num_i)
#     # 小数
#     num_f = i[i.rfind('.') + 1:].ljust(2, '0')
#     arguments.append(num_f)
# print(arguments)
# new_arg = " ".join(arguments)
# print(new_arg)
# SN = 'FF 42 53 00 15 49'
# sn = input("请扫码：")
# def tools(datas):
#     arguments = re.findall(".{2}", datas)
#     arguments = " ".join(arguments)
#     return arguments
# sn = tools(sn)
# middle = '03 0B 00 00 00 01 00 00 01' \
#          ' 00 00 00 00 00 00 ' \
#          '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ' + sn
# check_id = "%.2x" % (sum([int(sn, 16) for sn in middle.split(" ")]) % 256)
# print(check_id)




# min_set = public_var.config_dict.get('15')
# max_set = public_var.config_dict.get('16')
# before = [int(min_set),int(max_set)]
# f1 = lambda d: "%.2X" %(int(256-abs(d))) if (d<0) else "%.2X" %(d)
# after = []
# for i in before:
#     after.append(f1(i))
# print(after)
# new_arg = " ".join(after)
# print(new_arg)
# middle = '03 08 00 00 00 01'
# check_id = "%.2x" % (sum([int(sn, 16) for sn in middle.split(" ")]) % 256)
# print(check_id.upper())
# num1 = public_var.config_dict.get('1')
# num2 = public_var.config_dict.get('2')
# num3 = public_var.config_dict.get('3')
# num4 = public_var.config_dict.get('4')
# num5 = public_var.config_dict.get('9')
# num6 = public_var.config_dict.get('10')
# num7 = public_var.config_dict.get('7')
# num8 = public_var.config_dict.get('8')
# list2 = [num1,num2,num3,num4,num5,num6,num7,num8]
# print(list2)
# arguments = []
# config_value = []
# config_key = [1,2,3,4,9,10,7,8]
# for i in config_key:
#     num = public_var.config_dict.get(str(i))
#     config_value.append(num)
# for i in config_value:
#     if '.' not in i:
#         i = i + '.'
#     print(i,'*'*30)
#     # 整数
#     num_i = i[0:i.rfind('.')].rjust(2, '0')
#     arguments.append(num_i)
#     # 小数
#     num_f = i[i.rfind('.') + 1:].ljust(2, '0')
#     arguments.append(num_f)
# print(" ".join(arguments))
#
#
# a = '03 03 00 00 00 04 04 00 05 00 04 00 05 00 03 20 03 50 01 08 01 40'
# check_id = "%.2x" % (sum([int(sn, 16) for sn in a.split(" ")]) % 256)
# print(check_id)


# def csss(num):
#     num1_1 = num[0:num.rfind('.')].rjust(2,'0')
#     list1.append(num1_1)
#     num1_2 = num[num.rfind('.')+1:].ljust(2,'0')
#     list1.append(num1_2)
#     print(num1_1)
#     print(num1_2)



# 02 01 01 01 01 04 81 01 04 81 02 00 00 02 00 00
#
# a = -15
# print(hex(a),type(a))
# b = hex(15)