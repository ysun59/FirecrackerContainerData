# Firecracker and Container Data of Hotel Reservation

Specific setting and detailed vm and core corresponding can see the [Readme-v6.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v6.md) and [Readme-v8.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v8.md).

The firecrackers and containers in Readme-v6.md have the same setting, each vm set to one cpu core.

The firecreackers in Readme-v6.md each vm set to one, two or more cores.

## Greaphs
### CPU related
Use `


### Schedstat
Use `cat  /proc/schedstat` to generate "schedstat.txt".
Get the colume 7, 8, 9 of the cpu0 to 31
-

### Sched_debug
Use `cat /proc/sched_debug` to generate "schedDebug.txt".

### Interrupts
Use `cat /proc/interrupts` to generate "interrupts.txt".