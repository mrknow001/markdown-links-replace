import re,os,requests
import os.path

session = requests.Session()
session.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5
requests.packages.urllib3.disable_warnings()

filename = "文件名"

with open(filename+'.md','r+', encoding='UTF-8') as f:
    imgs = f.read()

if not os.path.exists(filename):
    os.mkdir(filename)

img_dict_l = {}
img_dict_r = {}
err_id = []

links = re.findall('(\[(.*)\]\((.*)\))',imgs)
img_dict_l.fromkeys(range(len(links),0))

for id,link in zip(range(len(links)),links):
    img_dict_l[id] = link[2]
    #print (str(id)+':'+link[2])


img_dict_r = dict(zip(img_dict_l.values(),img_dict_l.keys()))



for url_id in img_dict_l:
    try:
        print ('共'+str(len(links))+'张，正在下载'+str(url_id+1)+'张')
        response = requests.get(img_dict_l[url_id],verify=False)
        with open(filename+'/'+str(url_id)+'.jpg','wb') as fw:
            image = fw.write(response.content)
    except:
        print ('第'+str(url_id+1)+'张下载出错。匹配链接：'+img_dict_l[url_id])
        err_id.append(url_id)
        continue



for img_path in img_dict_r:
    if img_dict_r[img_path] in err_id:
        print (str(img_dict_r[img_path]+1)+'不替换')
    else:
        #print (img_path+'------------>'+filename+'/'+str(img_dict_r[img_path])+'.jpg')
        imgs = imgs.replace(img_path,filename+'/'+str(img_dict_r[img_path])+'.jpg')
        print ('第'+str(img_dict_r[img_path]+1)+'项替换完成')

with open(filename+'-新.md','w+', encoding='UTF-8') as f:
    f.write(imgs)
