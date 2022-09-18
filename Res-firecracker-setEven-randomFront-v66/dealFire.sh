#dealFire.sh
#!/bin/bash

for fcId in \
	firecracker_t_4_c_6_frontVcpu_1_wrkVcpu_1\
	firecracker_t_4_c_6_frontVcpu_1_wrkVcpu_2\
	firecracker_t_4_c_6_frontVcpu_2_wrkVcpu_1\
	firecracker_t_4_c_6_frontVcpu_2_wrkVcpu_2\
	firecracker_t_4_c_6_frontVcpu_4_wrkVcpu_1\
	firecracker_t_4_c_6_frontVcpu_4_wrkVcpu_2\
	firecracker_t_4_c_6_frontVcpu_6_wrkVcpu_1\
	firecracker_t_4_c_6_frontVcpu_6_wrkVcpu_2\
	firecracker_t_4_c_6_frontVcpu_8_wrkVcpu_1\
	firecracker_t_4_c_6_frontVcpu_8_wrkVcpu_2\
	firecracker_t_10_c_30_frontVcpu_1_wrkVcpu_1\
	firecracker_t_10_c_30_frontVcpu_1_wrkVcpu_2\
	firecracker_t_10_c_30_frontVcpu_2_wrkVcpu_1\
	firecracker_t_10_c_30_frontVcpu_2_wrkVcpu_2\
	firecracker_t_10_c_30_frontVcpu_4_wrkVcpu_1\
	firecracker_t_10_c_30_frontVcpu_4_wrkVcpu_2\
	firecracker_t_10_c_30_frontVcpu_6_wrkVcpu_1\
	firecracker_t_10_c_30_frontVcpu_6_wrkVcpu_2\
	firecracker_t_10_c_30_frontVcpu_8_wrkVcpu_1\
	firecracker_t_10_c_30_frontVcpu_8_wrkVcpu_2

do 
	echo $fcId
	cd $fcId
	cat wrk.txt|grep "Thread Stats"
	cat wrk.txt|grep "Latency  "
	cat wrk.txt|grep "Req/Sec  " 
	echo "----------#----------------#----------------"
	cat wrk.txt|grep "Socket errors"
	cat wrk.txt|grep "requests "
	cat wrk.txt|grep "Non-2xx"
	cat wrk.txt|grep "Requests/sec"
	cat wrk.txt|grep "Transfer/sec"
	echo ""
	cd ..
done
