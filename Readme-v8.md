# Hotel Reservation Data

let 13 firecrackers, each set to different cores, from core 0,2,4,6,8…….20

set frontend to core 1 or above (basically core 1,3,5-more-15)

set wrk to core 31, or 31, 29

## Overall CPU Excel
Can see the overall CPU utilization, throughtput, BW etc. in this excel https://docs.google.com/spreadsheets/d/1OmfJ4UT-Cw-CNSZ0VV-yk57sbN3G0qPgXfp6dItvTHI/edit#gid=365422113


## VMs - Corresponding cores
* consul \ -—-—----------------—------------------ core 0
* hotel-reserv-geo \ —---------------------------- core 2
* hotel-reserv-recommendation \ -——-—------------- core 4
* hotel-reserv-user \ —-------------—------------- core 6
* hotel-reserv-jaeger \ ----------—--------------- core 8
* hotel-reserv-rate-mmc \ ---------—-------------- core 10
* hotel-reserv-profile-mmc \ ----------—---------- core 12
* hotel-reserv-geo-mongo \ ----------—------------ core 14
* hotel-reserv-profile-mongo \ ------------------- core 16
* hotel-reserv-rate-mongo \ -----------—---------- core 18
* hotel-reserv-recommendation-mongo -------------- core 20

* hotel-reserv-reservation-mongo \ --------------- core 20
* hotel-reserv-user-mongo  ----------------------- core 20

* hotel-reserv-profile ---—----------------------- core 22, 24
* hotel-reserv-search --—------------------------- core 26, 28
* Hotel-reserv-rate —----------------------------- core 17, 19
* hotel-reserv-reservation —---------------------- core 21, 23
* hotel-reserv-reservation-mmc —---—---------------core 25, 27


## Generation Scrpts：
* test-CPU-randomCore-grayfox-firecracker
* test-CPU-oddEvenCore-grayfox-firecracker
不能直接用，config的xxx.yml里面cpus数量要改动的

## Data to use:
grayfox
~/yu/Res-DeathStartBench-data-V4-CPU-grayfox/xxx/

### Firecracker:
* Res-firecracker-random-in4-v8 (each firecracker ramdom limit run in 4 cores)
* Res-firecracker-random-in2-v8 (see "VMs - Corresponding cores" part)
* Res-firecracker-set-v8 (see "VMs - Corresponding cores" part)

Data in upper Res-firecracker-random-in2-v8 and Res-firecracker-set-v8 folders is using the same settings.
