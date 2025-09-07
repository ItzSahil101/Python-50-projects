import datetime
import time

endTime = datetime.datetime(2024,8,17)
site_block = ["www.wscubetech.com", "www.perplexity.ai"]

hostPath = "C:/Windows/System32/drivers/etc/hosts"
redirect= "127.0.0.1"

while True:
    if datetime.datetime.now() < endTime:
        print("***start Blocking***")
        with open(hostPath, "r+") as host_file:
            content = host_file.read()
            for web in site_block:
                if web not in content:
                    host_file.write(redirect +" "+web+"\n")
                else:
                    print("Website already blocked")
    else:
        with open(hostPath, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(web in lines for web in site_block):
                    host_file.write(lines)

            host_file.truncate()
        time.sleep(5)