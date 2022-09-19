# Firecracker and Container Data of Hotel Reservation

Specific setting and detailed vm and core corresponding can see the [Readme-v6.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v6.md) and [Readme-v8.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v8.md).

The firecrackers and containers in [Readme-v6.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v6.md)  have the same setting, each vm set to one cpu core.

The firecreackers in [Readme-v8.md](https://github.com/ysun59/FirecrackerContainerData/blob/master/Readme-v8.md) each vm set to one, two or more cores.

## Greaphs
### CPU related
Use `mpstat -P ALL 1` to generate "cpu_perf.txt".

Use fio_extract.py to deal data and get graphs.

- Graphs:
    - mpstat_all.png
    - mpstat_UsrSysEtc.png

### Schedstat
Use `cat  /proc/schedstat` to generate "schedstat.txt".

Use schedstat_extract.py to deal data and get graphs.

Get the colume 7, 8, 9 of the cpu0 to 31
- Meaning
    - Colume 9 means: # of tasks (not necessarily unique) given to the processor or means: # of timeslices run on this cpu.
    - Can refer to http://eaglet.pdxhosts.com/rick/linux/schedstat/v15/format-15.html or https://docs.kernel.org/scheduler/sched-stats.html for detailed info of colume 7, colume 8.
- Graphs:
    - schedstat_fig_col_7.png
    - schedstat_fig_col_8.png
    - schedstat_fig_col_9.png

### Sched_debug
Use `cat /proc/sched_debug` to generate "schedDebug.txt".

Use schedDebug_extract.py to deal data and get graphs.

Get the `.nr_switches` of each core.
- Graphs:
    - schedDebug_fig.png

### Interrupts
Use `cat /proc/interrupts` to generate "interrupts.txt".

Use interrupts_extract.py to deal data and get graphs.

Get the `RES: ....... Rescheduling interrupts` of each core.
- Graphs:
    - interrupts_fig.png