ls -1 log/test_best/*.out | xargs -I {} python wann_test.py -p p/biped.json -i {} | grep -E '^(nConn:|fitness:)' | tee biped_cons.txt
