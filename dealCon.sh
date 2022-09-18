#dealCon.sh
#!/bin/bash

for fcId in \
	container_t_4_c_6_frontCore_1_wrkCore_1\
	container_t_4_c_6_frontCore_1_wrkCore_2\
	container_t_4_c_6_frontCore_2_wrkCore_1\
	container_t_4_c_6_frontCore_2_wrkCore_2\
	container_t_4_c_6_frontCore_4_wrkCore_1\
	container_t_4_c_6_frontCore_4_wrkCore_2\
	container_t_4_c_6_frontCore_6_wrkCore_1\
	container_t_4_c_6_frontCore_6_wrkCore_2\
	container_t_4_c_6_frontCore_8_wrkCore_1\
	container_t_4_c_6_frontCore_8_wrkCore_2\
	container_t_10_c_30_frontCore_1_wrkCore_1\
	container_t_10_c_30_frontCore_1_wrkCore_2\
	container_t_10_c_30_frontCore_2_wrkCore_1\
	container_t_10_c_30_frontCore_2_wrkCore_2\
	container_t_10_c_30_frontCore_4_wrkCore_1\
	container_t_10_c_30_frontCore_4_wrkCore_2\
	container_t_10_c_30_frontCore_6_wrkCore_1\
	container_t_10_c_30_frontCore_6_wrkCore_2\
	container_t_10_c_30_frontCore_8_wrkCore_1\
	container_t_10_c_30_frontCore_8_wrkCore_2
do 
	echo $fcId
	cd $fcId
	cat wrk.txt|grep "Thread Stats"
	cat wrk.txt|grep "Latency  "
	cat wrk.txt|grep "Req/Sec " 
	echo "----------#----------------#----------------"
	cat wrk.txt|grep "Socket errors"
	cat wrk.txt|grep "requests "
	cat wrk.txt|grep "Requests/sec"
	cat wrk.txt|grep "Transfer/sec"
	echo ""
	cd ..
done
