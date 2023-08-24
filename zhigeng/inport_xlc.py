import xlrd
import requests
#靶场题目录入脚本兼容脚本手动选择平台及环境
# from input_url import attack_url,api,pub_api

# file=r'C:\Users\Shaopengyuan\Desktop\所有题库\微课堂考试选题(1).xlsx'
# header='TOKEN 72804e80366b4d539338d3dad043ccd4a164173c12a4eae5efadf2a4f8219f9b6ec73b8cbb1adb20a9d1e77f632c5c6cd1ec775a713a3db3289296c6977a7a7a'
# header='4a51cc29996f4801ac6924cf4ad8be44caecddfdbdeaeabdbaaddcbdcfbceeeafabfcafdfcfafdbadaaeedebfbaebeeafdaeffeefafdbdadabfaadcfedcebeeb'
app=['564d60e6ca9f4a5c920311cd42e37afcE92180Dd']
class Title_Entry():
    def __init__(self,file,header,platform,environment):
        """

        :param file: 文件路径
        :param header: 所需平台的header
        :param platform: 平台
        :param environment: 环境
        """

        self.attack_url = {
            "dev_url": "http://attack.dev.nosugar.io",  # 测试环境
            # "sim_url": "http://attack.sim.nosugar.tech",  # 线上测试
            "tech_url": "https://attack.nosugar.tech",  # 正式环境
            'sim_url':'https://attack-ccs.nosugar.tech',#ccs环境

            'api_list': ['/api/manager/main/question/list', '/api/manager/main/question/new',
                         '/api/manager/main/question/del'],  # 子平台

            "pub_dev_url": "http://attack-pub.dev.nosugar.io",  # 公共#测试环境
            "pub_sim_url": "http://attack-pub.sim.nosugar.tech",  # 公共#线上测试
            "pub_tech_url": "https://attack-pub.nosugar.tech",  # 公共#正式环境
            'put_api_list': ['/api/question/list', '/api/question/new', '/api/question/del'],  # 公共

            'res_id_list': ['id','hash_id'] ,# id 公共平台返回id
            'cc_id_list': ['id','question_id'] ,# id 公共平台传参id
            "Authorization": {"Authorization":header},        # 正式环境
            "Token": {"Token":header}# 正式环境

        }

        bool = xlrd.open_workbook(file)
        self.sheel = bool.sheet_by_index(0)
        self.h = self.sheel.nrows  # 获取行数
        self.session=requests.session()
        self.platform=platform
        self.environment=environment
    def sui(self):
        try:
            if self.platform=='put':
                self.de = self.attack_url ['put_api_list'][2]
                self.new = self.attack_url ['put_api_list'][1]
                self.list = self.attack_url ['put_api_list'][0]
                self.res_id=self.attack_url['res_id_list'][0]
                self.cc_id=self.attack_url['cc_id_list'][0]
                self.header=self.attack_url['Authorization']
                try:
                    if self.environment == 'dev':
                        self.url = self.attack_url['pub_dev_url']
                    elif self.environment == 'sim':
                        self.url = self.attack_url['pub_sim_url']
                    elif self.environment == 'tech':
                        self.url = self.attack_url['pub_tech_url']
                    else:
                        print('只能输入dev、sim、tech')

                except:
                    print('只能输入dev、sim、tech')
                return self.url, self.de, self.new, self.list, self.res_id,self.cc_id,self.header
            elif self.platform=='son':
                self.de = self.attack_url['api_list'][2]
                self.new = self.attack_url['api_list'][1]
                self.list = self.attack_url['api_list'][0]
                self.res_id = self.attack_url['res_id_list'][1]
                self.cc_id = self.attack_url['cc_id_list'][1]
                self.header = self.attack_url['Token']
                try:
                    if self.environment == 'dev':
                        self.url = self.attack_url['dev_url']
                    elif self.environment == 'sim':
                        self.url = self.attack_url['sim_url']
                    elif self.environment == 'tech':
                        self.url = self.attack_url['tech_url']
                    else:
                        print('只能输入dev、sim、tech')
                except :
                    print('只能输入dev、sim、tech')
                return self.url, self.de, self.new, self.list, self.res_id,self.cc_id,self.header
            else:
                print('只能输入put（公共）或  son（子平台）',1)

        except:
            print('只能输入put（公共）或  son（子平台）')
    def title_entry(self):
        list_datas=[]
        for i in range(1,self.h) :
            self.list_data = self.sheel.row_values(i)
            if self.list_data[5]!="":
                str_datas=self.list_data[5].replace(" ","@").split()
                lists = []
                for str_data in str_datas:
                    list_dat = str_data.replace("@", " ")
                    lists.append(list_dat)
                self.list_data[5] = lists
            try:
                self.list_data[6]=int(self.list_data[6])
            except:
                pass
            # if self.list_data[-1]!="":
                # print(self.list_data[-1])
            list_datas.append(self.list_data)
        # print(list_datas)
        return list_datas
    def requests_data(self,data,list_data,url,new,header):
        try:
            print(data)
            res = self.session.post(url=url+new, data=data, headers=header).json()

            if res['code'] == 200:
                print(f"{list_data}添加完成")
            else:
                print(f"{list_data}添加失败",res)
        except EnvironmentError as  e :
            print(f"{list_data} 导入失败,失败原因：{e}")
    def add(self):
        sui_data = self.sui()
        url = sui_data[0]
        new = sui_data[2]
        header = sui_data[6]
        list_datas=self.title_entry()
        i=1
        for list_data in list_datas:
            data={}
            self.res_msg=""
            # print(list_data)
            data['title'] = list_data[0]
            # data['question'] = "&lt;script&gt;&lt;/script&gt;"+list_data[1]  # 题目
            data['question'] = list_data[1]  # 题目
            data['tag'] = list_data[2]  # 内部标记
            if self.platform=='put':
                # data['question_type'] = list_data[3]  # question_type  qtype题目类型  essay   问答    radio  选择  file  文件  combo连协题
                # data['answer_type'] = list_data[4]  # answer_type  atype答案类型  dynamic  动态  raw 固定   human  人工判断
                question_type='question_type'
                answer_type='answer_type'
            else:
                # data['qtype'] = list_data[3]  # question_type  qtype题目类型  essay   问答    radio  选择  file  文件  combo连协题
                # data['atype'] = list_data[4]  # answer_type  atype答案类型  dynamic  动态  raw 固定   human  人工判断
                question_type = 'qtype'
                answer_type = 'atype'
            data[question_type] = list_data[3]  # question_type  qtype题目类型  essay   问答    radio  选择  file  文件  combo连协题
            data[answer_type] = list_data[4]  # answer_type  atype答案类型  dynamic  动态  raw 固定   human  人工判断
            data['options'] = list_data[5]  # 选项
            data['answer'] = list_data[6]  # 答案
            # data['env_id'] = list_data[7]  # 镜像
            # data['params'] = list_data[8]  # 镜像参数#镜像id
            data['difficulty'] = list_data[7] # 难度
            if  list_data[8]=="":
                data['points']=1
            else:
                data['points'] = list_data[8] # 积分
            data['tips'] = list_data[9]  # 解题提示
            data['method'] = list_data[10]  # 解题思路
            data['method'] = list_data[11]  # 坐标
            data['special_tip']=list_data[12]   #特别提示
            data['special_tip']=list_data[13]   #模拟调整
            if list_data[14]==''or list_data[14]==0:
                data['allow_skip']=0
            elif list_data[14]=='否'or list_data[14]==0:
                data['allow_skip'] = 0
            elif list_data[14]=='是'or list_data[14]==1:
                data['allow_skip'] = 1
            else:
                print('allow_skip传参错误')
            # data['allow_skip']=list_data[14]   #允许跳过  0默认不允许  1允许

            data['apps']=app#权限
            if data[question_type] =="单选题":
                data[question_type] = "radio"
                if data[answer_type]=="固定答案":
                    data[answer_type] = "raw"
                    if data['title']=='':
                        self.res_msg=f'第{i}条标题为空'
                        print(self.res_msg)
                        break
                    if data['question']=="":
                        self.res_msg =f'第{i}条题目为空'
                        print(self.res_msg)
                        break
                    if  data['options']=="":
                        self.res_msg = f'第{i}条选项为空'
                        print(self.res_msg)
                        break
                    if  data['answer']=="":
                        self.res_msg = f'第{i}条答案为空'
                        print(self.res_msg)
                        break
                    if  data['points']=="":
                        self.res_msg = f'第{i}条积分为空'
                        print(self.res_msg)
                        break
                    self.requests_data(data, list_data[0], url, new, header)
                else:
                    self.res_msg = f'第{i}条答案类型错误'
                    print(self.res_msg)
                    break
            elif data[question_type] =="问答题":
                del data['options']
                data[question_type] = "essay"
                if data[answer_type]=="固定答案":
                    data[answer_type] = "raw"
                    if data['title']=='':
                        self.res_msg=f'第{i}条标题为空'
                        print(self.res_msg)
                        break
                    if data['question']=="":
                        self.res_msg =f'第{i}条题目为空'
                        print(self.res_msg)
                        break
                    if  data['answer']=="":
                        self.res_msg = f'第{i}条答案为空'
                        print(self.res_msg)
                        break
                    if  data['points']=="":
                        self.res_msg = f'第{i}条积分为空'
                        print(self.res_msg)
                        break
                    self.requests_data(data, list_data[0], url, new, header)
                else:
                    self.res_msg = f'第{i}条答案类型错误'
                    print(self.res_msg)
                    break
            else:
                self.res_msg = f'第{i}条题目类型错误'
                print(self.res_msg)
                break
            print(f"已添加{i}条")
            i+=1
        res={"num":i-1,"msg":self.res_msg}
        return res
    def dele(self,title=None):
        sui_data= self.sui()
        url = sui_data[0]
        de = sui_data[1]
        new = sui_data[2]
        list = sui_data[3]
        res_id = sui_data[4]
        cc_id = sui_data[5]
        header = sui_data[6]
        if title==None:
            data = {"page_size": 10, "page": 1}
        else:
            data = {"title": title, "page_size": 10, "page": 1}
        res = self.session.post(url=url+list, data=data, headers=header).json()
        # print(res)
        total = res["pagination"]['total']
        if total%10 ==0:
            page = int(total/10)
        else:
            page = int(total / 10) + 1
        q = 1
        for i in range(1, page + 1):
            res1 = self.session.post(url=url +  list, data=data,
                                    headers=header).json()
            datas = res1["data"]
            for dat in datas:
                question_id = dat[res_id]
                res = self.session.post(url=url + de, data={cc_id: question_id},
                                        headers=header).json()  # question_id
                if res['code'] == 200:
                    print(q, "删除成功")
                else:
                    print(f"第{i}条删除失败，{res}")
                q += 1



# if __name__ == '__main__':
#     s=Delete('son','dev','ca76029528cb4193b2a5170fa4ce3180aacacedafdddadcaefecdbdaceeedecedbffdcffeeabdabcbcfbcadaddfedcfaaadbcffabbeeccbdeccaeafcaeacbddc',
#          '黑话1')
#     ss=s.del_ti()
# y=Title_Entry(file,header)
# s=y.title_entry()
# y.sui()
# y.add()
# Del().dele("测试")
# Del().dele()
# y.dele("调证公司")
# t=Title_Entry()