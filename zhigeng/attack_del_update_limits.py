import requests
#删除题目  编辑题目权限
class Topic_Del_Update():
    # def __init__(self,platform,environment,header,title=None,question=None,tag=None):
    def __init__(self,platform,environment,header):
        self.attack_url = {
            "dev_url": "http://attack.dev.nosugar.io",  # 测试环境
            # "sim_url": "http://attack.sim.nosugar.tech",  # 线上测试
            "tech_url": "https://attack.nosugar.tech",  # 正式环境
            'sim_url': 'https://attack-ccs.nosugar.tech',  # ccs环境

            'api_list': ['/api/manager/main/question/list', '/api/manager/main/question/new',
                         '/api/manager/main/question/del'],  # 子平台

            "pub_dev_url": "http://attack-pub.dev.nosugar.io",  # 公共#测试环境
            "pub_sim_url": "http://attack-pub.sim.nosugar.tech",  # 公共#线上测试
            "pub_tech_url": "https://attack-pub.nosugar.tech",  # 公共#正式环境
            'put_api_list': ['/api/question/list', '/api/question/new', '/api/question/del','/api/question/save'],  # 公共

            'res_id_list': ['id', 'hash_id'],  # id 公共平台返回id
            'cc_id_list': ['id', 'question_id'],  # id 公共平台传参id
            "Authorization": {"Authorization": header},  # 正式环境
            "Token": {"Token": header}  # 正式环境

        }
        try:
            if platform=='put':
                self.update = self.attack_url['put_api_list'][3]
                self.de = self.attack_url ['put_api_list'][2]
                self.new = self.attack_url ['put_api_list'][1]
                self.list = self.attack_url ['put_api_list'][0]
                self.res_id=self.attack_url['res_id_list'][0]
                self.cc_id=self.attack_url['cc_id_list'][0]
                self.header=self.attack_url['Authorization']
                try:
                    if environment == 'dev':
                        self.url = self.attack_url['pub_dev_url']
                    elif environment == 'sim':
                        self.url = self.attack_url['pub_sim_url']
                    elif environment == 'tech':
                        self.url = self.attack_url['pub_tech_url']
                    else:
                        print('只能输入dev、sim、tech')
                except:
                    print('只能输入dev、sim、tech')
            elif platform == 'son':
                self.de = self.attack_url['api_list'][2]
                self.new = self.attack_url['api_list'][1]
                self.list = self.attack_url['api_list'][0]
                self.res_id = self.attack_url['res_id_list'][1]
                self.cc_id = self.attack_url['cc_id_list'][1]
                self.header = self.attack_url['Token']
                try:
                    if environment == 'dev':
                        self.url = self.attack_url['dev_url']
                    elif environment == 'sim':
                        self.url = self.attack_url['sim_url']
                    elif environment == 'tech':
                        self.url = self.attack_url['tech_url']
                    else:
                        print('只能输入dev、sim、tech')
                except:
                    print('只能输入dev、sim、tech')
        except Exception as e:
            print(f'只能输入put（公共）或  son（子平台）{e}')
        self.session=requests.session()
        self.data = {
            "page": 1,
            "page_size": 10
        }

    def del_ti(self,title=None,question=None,tag=None):
        if self.data['title']==None:
            del self.data['title']
        if self.data['question']==None:
            del self.data['question']
        if self.data['tag']==None:
            del self.data['tag']
        self.data["title"]=title
        self.data["question"]=question
        self.data["tag"]=tag
        de_res={}
        i=1
        try:
            res_list = self.session.post(url=self.url+self.list, data=self.data, headers=self.header).json()
            if res_list['pagination']['total']!=0:
                if res_list['pagination']['total']%10 ==0:
                    total=int(res_list['pagination']['total']/10)
                else:
                    total = int(res_list['pagination']['total']/10+1)
                for  tot  in range(total):
                    res = self.session.post(url=self.url + self.list, data=self.data, headers=self.header).json()
                    datas=res['data']
                    if datas != []:
                        for data in datas:
                            de_data={self.cc_id:data[self.res_id]}
                            self.session.post(url=self.url + self.de, data=de_data, headers=self.header).json()
                            print(f'正在删除第{i}条,标题为{data["title"]}')
                            i+=1
                        print(f'成功删除{i-1}条')
                        msg = f'成功删除{i-1}条'
                        code=200
                        de_res = {"num": i - 1, "msg": msg, "code": code}
            else:
                msg = '没有搜索到结果'
                code = 403
                de_res = {"num": 0, "msg": msg, "code": code}
            return de_res
        except Exception as  e :
            msg = f'{e}'
            code = 500
            # de_res = [i-1, msg,code]
            de_res={"num": 0, "msg": msg, "code": code}
            return de_res
    def update_ti(self,app_id):
        de_res={}
        update_res={}
        msg =""
        i=1

        try:
            res_list = self.session.post(url=self.url+self.list, data=self.data, headers=self.header).json()
            try:
                print(res_list['pagination']['total'])
            except Exception as e :
                msg='参数错误'
                update_res = {"num": i, "msg": msg, "code": 403}
                return update_res
            if res_list['pagination']['total'] != 0:
                if res_list['pagination']['total']%10 ==0:
                    self.total=int(res_list['pagination']['total']/10)
                else:
                    self.total = int(res_list['pagination']['total']/10+1)
                for   to in range(1,self.total+1):
                    de_res['page']=to
                    de_res['page_size']=10
                    res_list = self.session.post(url=self.url + self.list, data=de_res, headers=self.header).json()
                    for  res_list_data in  res_list['data']:
                        ids = []
                        files = []
                        if res_list_data['apps'] != []:
                            for id in res_list_data['apps']:
                                ids.append(id['id'])
                        ids.append(app_id)
                        res_list_data['apps']=ids
                        if res_list_data['files'] !=[]:
                            for  fil in res_list_data['files']:
                                files.append(fil['id'])
                            res_list_data['files']=files
                        del res_list_data['created_at']
                        del res_list_data['updated_at']
                        del res_list_data['creator']
                        del res_list_data['alive_count']
                        if res_list_data['env_id'] == "":
                            del res_list_data['env_id']
                        if res_list_data['multi_answer'] == []:
                            del res_list_data['multi_answer']
                        if res_list_data['images'] == []:
                            del res_list_data['images']
                        if res_list_data['image_params'] == []:
                            del res_list_data['image_params']
                        if res_list_data['position'] == "":
                            res_list_data['position']=[]
                        # print(res_list_data['apps'])
                        # print(res_list_data,1111111)
                        res_list = self.session.post(url=self.url + self.update, data=res_list_data, headers=self.header).json()
                        # print(res_list,11111111111111)
                        msg=f'添加权限完成,已添加{i}条'
                        print(res_list['data']['status'],f'{res_list_data["title"]}添加权限完成,已添加{i}条')
                        i+=1
            else:
                update_res = {"num": i, "msg": "可修改题目为0", "code": 403}
                return update_res
        except Exception as  e :
            msg = f'错误：{e}'
            code = 500
            # de_res = [i-1, msg,code]
            print(i,e)
            update_res={"num": i, "msg": msg, "code": code}
            return update_res

        update_res = {"num": i, "msg": msg, "code": 200}
        return  update_res
# if __name__ == '__main__':
#     # platform, environment, header, title = None, question = None, tag = None):
#     app_id='3099f77ca84b4aa8991ae17719d1cd84cb495f0f'
#     t=Topic_Del_Update('put',environment='dev',header='TOKEN 6cb6153939e04e23ad4462c8e8d612796b173de54a75e856ebe8dbf488b43dbce834fb749e5b1ec584945eb5b15c6fc09a7c7abb6a600a44e139da71e43b4dc5')
#     t.update_ti(app_id)