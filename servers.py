import speedtest

s = speedtest.Speedtest()
servers = s.get_servers()
s.get_servers(servers)
