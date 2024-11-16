import json

import httpx

import base64


# لینک Shadowsocks
ss_link = "ss://YWVzLTI1Ni1nY206YVNsNVp1b0pRcEA0Ni4xMDEuMjUxLjMyOjIxMDEw@fsdjbfhjdf"

# جدا کردن بخش رمزگذاری شده
encoded_part = ss_link.split('ss://')[1].split('@')[0]

# رمزگشایی Base64
decoded_bytes = base64.urlsafe_b64decode(encoded_part + '==')
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

decoded_str = decoded_bytes.decode('utf-8')

print( decoded_str)


def GetConfig(stream:dict, uuid: str, email: str, port: str, protocol: str, serverName: str):
    # Your Remark
    inboundSetting = json.loads(stream['streamSettings'])
  
    remark = email

    path = None
    host = "none"
    domainName = None
    serviceName = None
    headerType = None
    alpn = None
    kcpType = None
    grpcSecurity = None
    
   # Get Security 
    fingerPrint = ""
   
    tls = inboundSetting["security"]

    if  tls == "reality":
      
 
      fingerPrint = inboundSetting['realitySettings']['settings']['fingerprint']
      global publicKey 
      publicKey =  inboundSetting['realitySettings']['settings']['publicKey']
      global shortIds
      shortIds = inboundSetting['realitySettings']['shortIds'][0]
      global spiderX
      spiderX = inboundSetting['realitySettings']['settings']['spiderX']
      global sni
      sni = inboundSetting['realitySettings']['serverNames'][0]
  
    if tls == "tls":
        domainName = inboundSetting["tlsSettings"]["serverName"]
    elif tls == "xtls":
        domainName = inboundSetting["xtlsSettings"]["serverName"]
        alpn =  inboundSetting["tlsSettings"][0]["certificates"]["alpn"][0]
        global allowInsecure 

        allowInsecure = inboundSetting["tlsSettings"][0]["certificates"]["allowInsecure"]
   
   
   #    Get Net Type Setting
    netType = inboundSetting["network"]
    if netType == "grpc":
        serviceName = inboundSetting["grpcSettings"]["serviceName"]
        grpcSecurity = inboundSetting["security"]
    elif netType == "tcp":
        headerType = inboundSetting["tcpSettings"]["header"]["type"]
        if headerType != "none":
            
          path = inboundSetting["tcpSettings"]["header"]["request"]["path"][0]
          try:
              
             host = inboundSetting["tcpSettings"]["header"]["request"]["headers"]["host"][0]
          except:
             host = inboundSetting["tcpSettings"]["header"]["request"]["headers"]["Host"][0]
                 
    elif netType == "ws":
       
        path = inboundSetting["wsSettings"]["path"]
        try:
            host = inboundSetting["wsSettings"]["headers"]["host"]
        except:
            host=""    
    elif netType == "kcp":
        kcpType = inboundSetting["kcpSettings"]["header"]["type"]
        kcpSeed = inboundSetting["kcpSettings"]["seed"]




    #  Get Protocol . Final Step 
    if protocol == "shadowsocks":
       setting = json.loads(stream['settings'])
       confFirst = f"{setting['method']}:{setting['password']}:{uuid}"
       Clients = ""
       decoded_bytes = base64.urlsafe_b64encode(confFirst )
       if tls == "tls":
             conf += f"&security={tls}&fp={fingerPrint}&alpn={alpn}{'&allowInsecure=1' if allowInsecure ==True else'' }&sni={sni}"
       if netType == "tcp" : return  f"{protocol}://{decoded_bytes}@{serverName}:{port}?type={netType}{f'&headerType={headerType}&path= {path if path!="" else"/"}&host={host}' if headerType != "none" else ''}{conf}#{remark} "

       elif netType == "ws" or netType == "httpupgrade" or netType == "splithttp" : return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&path= {path if path!="" else"/"}&host={host}{conf}#{remark}"
                      
       elif netType == "kcp": return  f"{protocol}://{decoded_bytes}@{serverName}:{port}?type={netType}&security={tls}&headerType={kcpType}&seed={kcpSeed}#{remark}"             
            
       if netType == "grpc":
            
            authority = inboundSetting['grpcSettings']['authority']
           
            conf  = f"&serviceName={serviceName}&authority={authority}" + conf
            

            return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}{f'&headerType={headerType}&path= {path if path!="" else"/"}&host={host}' if headerType != "none" else ''}{conf}#{remark} "


 
 
    if protocol == "trojan":
        conf = ""
        if tls == "reality":
               conf += f"security={tls}&pbk={publicKey}&fp={fingerPrint}&sni={sni}&sid={shortIds}&spx={spiderX}"             
        if tls == "tls":
             conf += f"&security={tls}&fp={fingerPrint}&alpn={alpn}{'&allowInsecure=1' if allowInsecure ==True else'' }&sni={sni}"
        if netType == "tcp" : return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}{f'&headerType={headerType}&path= {path if path!="" else"/"}&host={host}' if headerType != "none" else ''}{conf}#{remark} "

        elif netType == "ws" or netType == "httpupgrade" or netType == "splithttp" : return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&path= {path if path!="" else"/"}&host={host}{conf}#{remark}"
                      
        elif netType == "kcp": return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&security={tls}&headerType={kcpType}&seed={kcpSeed}#{remark}"             
            
        if netType == "grpc":
            
            authority = inboundSetting['grpcSettings']['authority']
           
            conf  = f"&serviceName={serviceName}&authority={authority}" + conf
            

            return  f"{protocol}://{uuid}@{serverName}:{port}?type={netType}{f'&headerType={headerType}&path= {path if path!="" else"/"}&host={host}' if headerType != "none" else ''}{conf}#{remark} "
    elif protocol == "vless":
        conf = ""
        if netType == "tcp":
            if headerType == "http":
                conf += "&headerType=http"
            if tls == "xtls":
                conf += f"&security={tls}&flow=xtls-rprx-direct"
            if tls == "reality":
               conf += f"security={tls}&pbk={publicKey}&fp={fingerPrint}&sni={sni}&sid={shortIds}&spx={spiderX}"     
            if tls == "tls":
             conf += f"&security={tls}&fp={fingerPrint}&alpn={alpn}{'&allowInsecure=1' if allowInsecure ==True else'' }&sni={sni}"
            if host =="none" :
                host=""    
            newConfig = f"{protocol}://{uuid}@{serverName}:{port}?type={netType}{f'&headerType={headerType}&path= {path if path!="" else"/"}&host={host}' if headerType != "none" else ''}{conf}#{remark} "
        elif netType == "ws":
            if tls == "tls":
             
             conf += f"&security={tls}&fp={fingerPrint}&alpn={alpn}{'&allowInsecure=1' if allowInsecure == True else'' }&sni={sni}"

            newConfig = f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&path={path if path!="" else"/"}&host={host}{conf}#{remark} "
        elif netType == "kcp":
            newConfig = f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&security={tls}&headerType={kcpType}&seed={kcpSeed}#{remark}"
        elif netType == "grpc":
             
            authority = inboundSetting['grpcSettings']['authority']
           
            conf  = f"&serviceName={serviceName}&authority={authority}" + conf
            if tls == "xtls":
                conf += "&flow=xtls-rprx-direct"
            if tls == "reality":
               conf += f"security={tls}&pbk={publicKey}&fp={fingerPrint}&sni={sni}&sid={shortIds}&spx={spiderX}"     
            if tls == "tls":
             conf += f"&security={tls}&fp={fingerPrint}&alpn={alpn}{'&allowInsecure=1' if allowInsecure ==True else'' }&sni={sni}"
            newConfig = f"{protocol}://{uuid}@{serverName}:{port}?type={netType}&serviceName={serviceName}#{remark}"
    elif protocol == "vmess":
        vmessConf = {
            "v": "2",
            "ps": f"{remark}",
            "add": serverName,
            "port": int(port),
            "id": uuid,
            "aid": 0,
            "net": netType,
            "type": "none",
            "tls": "none",
            "path": "",
            "host":  ""

        }
     
   
        if headerType != None:
            vmessConf["type"] = headerType
        elif kcpType != None:
            vmessConf["type"] = kcpType
        else:
            vmessConf["type"] = "none"

        if host != None or host != "none":
            vmessConf["host"] = host
        if path == None or path == '':
            vmessConf["path"] = "/"
        else:
            vmessConf["path"] = path
        if  tls == "" or tls =="none":
            vmessConf["tls"] = "none"

        else:
            vmessConf["tls"] = tls
        if headerType == "http":
            vmessConf["path"] = "/"
            vmessConf["type"] = headerType
        if netType == "kcp":
            if kcpSeed != None or kcpSeed != "":
                vmessConf["path"] = kcpSeed

        if netType == "grpc":
            vmessConf['type'] = grpcSecurity
            vmessConf['scy'] = 'auto'
        if netType == "httpupgrade" or netType == "splithttp":
              vmessConf['scy'] = 'auto'
        res = json.dumps(vmessConf)
        res =res[1:]

        res = "{\n"  +  res.replace("}","\n}")
        res = res.replace("," ,",\n ")
        sample_string_bytes = res.encode("ascii")
    
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        
        newConfig = f"vmess://{base64_string}"
    return newConfig

gonfig = GetConfig("{\n  \"network\": \"tcp\",\n  \"security\": \"tls\",\n  \"externalProxy\": [],\n  \"tlsSettings\": {\n    \"serverName\": \"ali.com\",\n    \"minVersion\": \"1.2\",\n    \"maxVersion\": \"1.3\",\n    \"cipherSuites\": \"\",\n    \"rejectUnknownSni\": false,\n    \"disableSystemRoot\": false,\n    \"enableSessionResumption\": false,\n    \"certificates\": [\n      {\n        \"certificateFile\": \"ihjbk n\",\n        \"keyFile\": \"bljk\",\n        \"ocspStapling\": 3600,\n        \"oneTimeLoading\": false,\n        \"usage\": \"encipherment\",\n        \"buildChain\": false\n      }\n    ],\n    \"alpn\": [\n      \"h3\",\n      \"h2\",\n      \"http/1.1\"\n    ],\n    \"settings\": {\n      \"allowInsecure\": true,\n      \"fingerprint\": \"chrome\"\n    }\n  },\n  \"tcpSettings\": {\n    \"acceptProxyProtocol\": false,\n    \"header\": {\n      \"type\": \"none\"\n    }\n  }\n}","96e4a691-cf74-44d4-b728-c9c5cee5e59e","ARS","59964","vless","188.245.191.197")

import requests

url = "http://188.245.191.197:8282/21B3KxL4LFPvxQT/panel/inbound/list"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'Origin': 'http://188.245.191.197:8282',
  'Connection': 'keep-alive',
  'Referer': 'http://188.245.191.197:8282/21B3KxL4LFPvxQT/panel/inbounds',
  'Cookie': 'lang=en-US; 3x-ui=MTczMTMzMzI3NHxEWDhFQVFMX2dBQUJFQUVRQUFCMV80QUFBUVp6ZEhKcGJtY01EQUFLVEU5SFNVNWZWVk5GVWhoNExYVnBMMlJoZEdGaVlYTmxMMjF2WkdWc0xsVnpaWExfZ1FNQkFRUlZjMlZ5QWYtQ0FBRUVBUUpKWkFFRUFBRUlWWE5sY201aGJXVUJEQUFCQ0ZCaGMzTjNiM0prQVF3QUFRdE1iMmRwYmxObFkzSmxkQUVNQUFBQUh2LUNHd0VDQVFvMGF6ZHhNREZvWkZZeUFRcFpNMU5IUWtod2JVcHNBQT09fKGIEMa3XL2Q5o6LnOVouUn21wApxAEdh_8wvq8kKtmA',
  'Content-Length': '0'
}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# dataConveerted = json.loads(response.text)


print(gonfig)