let 18 firecrackers, each set to different cores, from core 0,2,4,6,8..30
set frontend to core 1 or above (basically core 1,3,5-more)
Set wrk to core 31 or 31, 29


consul \ —--- core 0
  hotel-reserv-profile \    —--- core 2
  hotel-reserv-search \   —--- core 4
  hotel-reserv-geo \        —--- core 6
  hotel-reserv-rate \        —--- core 8
  hotel-reserv-recommendation \       —--- core 10
  hotel-reserv-user \       —--------------—--- core 12
  hotel-reserv-reservation \              -—--- core 14
  hotel-reserv-jaeger \      —--------——--- core 16
  hotel-reserv-rate-mmc \       —------------ core 18
  hotel-reserv-profile-mmc \       —---------- core 20
  hotel-reserv-reservation-mmc \      -—--- core 22
  hotel-reserv-geo-mongo \       —----------- core 24
  hotel-reserv-profile-mongo \       —-------- core 26
  hotel-reserv-rate-mongo \       —----------- core 28
  hotel-reserv-recommendation-mongo \  —-----------core 30

  hotel-reserv-reservation-mongo \ —-----------core 30
  hotel-reserv-user-mongo	 —-----------core 30




脚本：
test-CPU-randomCore-grayfox
test-CPU-oddEvenCore-grayfox
test-CPU-setEvenCore-randomFront-grayfox


Data to use:
grayfox
~/yu/Res-DeathStartBench-data-V4-CPU-grayfox/xxx/

Container:
Res-container-random-v6            
Res-container-set-v6              
Res-container-setEven-randomFront-v6 

Firecracker:
Res-firecracker-random-v7 
Res-firecracker-set-v7 
Res-firecracker-setEven-randomFront-v7

