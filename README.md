# python-esther
Python simulation files for ESTHER Shock Tube

```
cat streaming_config_tcp_16
host 192.168.10.10
port 8900
protocol 1
rate 16
channels 1
resolution 2
use_file 0
format 0
samples 2000000000


./rpsa_client -h 192.168.10.10 -p TCP -f ./ -t csv -s 16000000
```

