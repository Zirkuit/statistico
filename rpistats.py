from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if os.path.exists("/index.html"):
            os.remove("/index.html")
        f = open("index.html", "w")
        f.write('<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content=$
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True )
        cmd = "uptime"
        uptime = subprocess.check_output(cmd, shell = True )
        f.write("<p>IP Adress: " + str(IP) + "</p>")
        f.write("<p>CPU Usage: " + str(CPU) + "</p>")
        f.write("<p>Memory Usage: " + str(MemUsage) + "</p>")
        f.write("<p>Disk Usage: " + str(Disk) + "</p>")
        f.write("<p>Uptime: " + str(uptime) + "</p>")
        f.write("</body></html>")
        f.close()
        self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('192.168.0.16', 8080), Serv)
httpd.serve_forever()