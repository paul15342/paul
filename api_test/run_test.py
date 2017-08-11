import openpyxl
import os,time
import xlwt
from wirte_excel import *
from get_token import *

success_num = 0
error_num = 0

def get_excel():
    dict ={}
    host = "http://192.168.50.21:8181"
    p = os.getcwd()
    path = p + '/data/param.xlsx'
    E = openpyxl.load_workbook(path)
    sheets = E.get_sheet_names()
    sheet = E.get_sheet_by_name(sheets[0])
    rows = sheet.max_row
    list = []
    for i in range (2,rows+1):
        param = sheet['D{}'.format(i)].value
        url = host + sheet['C{}'.format(i)].value
        exjson =sheet['E{}'.format(i)].value
        dict ={"param":param,'url':url,"exjson":exjson}
        list.append(dict)
    return list


def run(url,param):
    request = Api().get_session()
    res = request.post(url,data=param)
    text = json.loads(res.text)
    code = text['code']
    status_code = res.status_code
    return status_code, code


def compare(realStatus_code,real_code,ex_code,exStatus_code=200):
    global success_num,error_num
    if realStatus_code == exStatus_code and real_code == ex_code:

        success_num += 1
        print ('PASS')
        return True
    else:
        error_num += 1
        print('error')
        return False

def main():
    list = get_excel()
    global success_num,error_num

    for i in range(len(list)):
        url = list[i]['url']
        param = eval(list[i]['param'])
        param["token"] = Api().get_token()
        exjson = eval(list[i]['exjson'])
        ex_code = exjson['code']
        print('==========================================')
        realStatus_code, real_code = run(url, param)
        print("ex_code: {}".format(ex_code))
        print("real_code: {}".format(real_code))
        if compare(realStatus_code, real_code, ex_code):       #根据compare返回true,在Excel中写入PASS
            Excel.write_result_success(i)
        else:
            Excel.write_result_fail(i)                         #根据compare返回false,在Excel种写入Fail



    print ("="*50)
    print("total:{}".format(len(list)))
    print("error_num: {}".format(error_num))
    print('success_num: {}'.format(success_num))
    Excel.save()

if __name__=="__main__":
    print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    main()
