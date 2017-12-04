sll $t2, $s0, 4
beq $t0, $t1, L1
lw $s0, -8 ($t1)
L1:add $s1 , $s2 , $s3