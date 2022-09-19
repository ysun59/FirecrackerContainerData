#dealFire.sh
#!/bin/bash

cp dealCon.sh Res-container-random-v6
cp dealCon.sh Res-container-set-v6
cp dealCon.sh Res-container-setEven-randomFront-v6 
cp dealFire.sh Res-firecracker-random-in2-v8
cp dealFire.sh Res-firecracker-random-in4-v8
cp dealFire.sh Res-firecracker-random-v66
cp dealFire.sh Res-firecracker-set-v66
cp dealFire.sh Res-firecracker-set-v8 
cp dealFire.sh Res-firecracker-setEven-randomFront-v66

for folder in \
    Res-container-random-v6\
    Res-container-set-v6 \
    Res-container-setEven-randomFront-v6\
    Res-firecracker-random-in2-v8\
    Res-firecracker-random-in4-v8\
    Res-firecracker-random-v66\
    Res-firecracker-set-v66\
    Res-firecracker-set-v8\
    Res-firecracker-setEven-randomFront-v66
do
    cp *.py $folder
    cd $folder
    python3 fio_extract.py
    python3 interrupts_extract.py
    python3 schedDebug_extract.py
    python3 schedstat_extract.py
    cd ..
done

