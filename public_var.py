com_port = ''
bps = 0
config_dict = {}
config_name = {'0':'order_id','1':'min_txd','2':'max_txd','3':'min_sta','4':'max_sta','5':'min_cap','6':'max_cap',
              '7':'min_1.2v','8':'max_1.2v','9':'min_3.3v','10':'max_3.3v','11':'min_12vboost','12':'max_12vboost',
              '13':'min_damping','14':'max_damping','15':'min_fre_offset','16':'max_fre_offset','17':'min_set_static',
              '18':'max_set_static','19':'min_set_dynamic','20':'max_set_dynamic','21':'soft_version','22':'version'}

burn_flag = False
# pro_test_flag = False
ftp_flag = False
config_flag = {}
bin_src = ''
dev_id = {}
# 软硬件版本,PIN电压,通讯,频偏,过零,功耗,停电上报,写ID
test_option = {'0':False,'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False}
order_id = ''
first_step = False
second_step = False
third_step = False
fourth_step = False
end_order = ''