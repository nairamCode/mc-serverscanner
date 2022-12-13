# mc-serverscanner
It scanns ips if they are mc servers. If they are it will ping them and store the response.

# Description
This Code is an adition to the [ips scanner](https://github.com/nairamCode/Reading-Ips-form-an-binary-file) I've made. So better take a look on that first. This script does the following things:
  1. Read the Ip from the binary file [(ips scanner)](https://github.com/nairamCode/Reading-Ips-form-an-binary-file)
  2. Checks if the ip is already in the server_scan.txt (so you don't have to scan the hole list again every time)
  3. Ping the ip
  4. write the response in the server_scan.txt
  5. again

# Credits
[Criptc](https://github.com/Criptc) (he wrote the ["pinger"](https://github.com/Criptc/minecraft-handmade-headless-client) I used)
