add $s1 , $s2 , $s3
and $s1 , $s2 , $s3
beq $t0, $t1, L2
sll $t2, $s0, 4
sw  $t0, 0 ($t1)
L2: add $s1 , $s2 , $s3