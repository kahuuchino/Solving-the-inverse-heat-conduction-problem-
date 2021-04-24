SET ANS_CONSEC=YES
SET ANSYS_LOCK=OFF
SET KMP_STACKSIZE=2048k
"D:\ANSYS Inc\v211\ansys\bin\winx64\MAPDL.exe"  -p ansys -dis -mpi INTELMPI -np 2 -lch -dir "D:\Graduation Project\APDL Files\revue" -j "revue" -s read -l en-us -b -i "D:\Graduation Project\Arithmetic\modify.txt" -o "D:\Graduation Project\APDL Files\revue\temp.out"
copy "D:\Graduation Project\APDL Files\revue\temp.dat" "D:\Graduation Project\Arithmetic" /Y