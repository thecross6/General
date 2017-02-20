	.data
	J: .word 10
	x: .word 1
	newline: .asciiz "\n"
	.text
	la $t0, x # Load x = 1
	la $t1, J # Load J = 10
	lw $t0, 0($t0)
	lw $t1, 0($t1)
loop:	mul $t2, $t0, 3
	addi $t0, $t2, 1
	addi $a0, $t0, 0
	li $v0, 1
	syscall
	la $a0, newline
	li $v0, 4
	syscall
	subi $t1, $t1, 1
	bgtz $t1, loop 