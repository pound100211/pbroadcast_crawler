import requests
import time
import threading
import sys

def req(num,name):
	#name = {'001':'zgzs','002':"jjzs","003":"yyzs"}
	#url = "http://ngcdn{1}.cnr.cn/live/{2}/index.m3u8".format()
	url = "http://ngcdn{n1}.cnr.cn/live/{n2}/index.m3u8".format(n1=num,n2=name)
	try:
		r = requests.get(url)
	except e:
		print("request failed")
		return e
	if r.status_code != 200:
		print("request refused!")
		return e
	#print(r.status_code)
	#print(r.text)
	return r.text, int(r.text[47:55])

def download(text,num,name,txtname):
	'''
	text = #EXTM3U
	#EXT-X-VERSION:3
	#EXT-X-MEDIA-SEQUENCE:2789210
	#EXT-X-TARGETDURATION:10
	#EXTINF:10.006,
	2789210.ts
	#EXTINF:10.005,
	2789211.ts
	#EXTINF:10.005,
	2789212.ts
	#EXTINF:10.006,
	2789213.ts
	#EXTINF:10.005,
	2789214.ts
	#EXTINF:10.005,
	2789215.ts
	'''
	
	t = time.asctime(time.localtime(time.time()))
	#t = time.
	url = ""
	#txtname = "./{}{}/file{}.txt".format(num,name,t)
	i = 96
	while i<250:
		url = "http://ngcdn{n1}.cnr.cn/live/{n2}/{n3}".format(n1=num,n2=name,n3=text[i:i+10])
		file1 = requests.get(url)
		path = "./"+num+name+"/"+num+name+text[i:i+10]
		with open(path,"wb") as f :
			f.write(file1.content)
		txtcontent = "file {}{}{}".format(num,name,text[i:i+10])
		with open(txtname,'a') as f:
			f.write(txtcontent+'\n')
			f.close()
		#print(text[i:i+10])
		i=i+27
	print(t)
	print("download {n3} 6 files success".format(n3=text[47:54]))
	return int(text[47:55])


def do_crawl(num,name):
	media_seqold = 0
	t = time.asctime(time.localtime(time.time()))
	txtname = "./{}{}/file{}.txt".format(num,name,t)
	while 1 :
		
		r, media_seqnew  = req(num,name)

		if media_seqnew >= media_seqold+6 or media_seqold ==  0:
			media_seqold = media_seqnew
			download(r,num,name,txtname)
		time.sleep(59)

	




if __name__ == '__main__':
	_, num, name = sys.argv
	print(num,name)

	do_crawl(num,name)
	
	
	
	
	
	
	
	
	
	
	
	
	

