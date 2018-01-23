; I have a great interest in assembly language for multiple reasons, one of which is Dr. Knuth's MIX and MMIX computers, and
; another for simply the nerd factor. This is my attempt to display 'hello world' in asm in Linux. It compiles, but I have no 
; idea if it's even functional, because it doesn't output to the terminal.

.text
  .global _start
  
_start:
    
  movl $len, %edx
  movl $msg, %ecx
  movl $1, %ebx
  movl $4, %eax
  int $0x80
	
  movl $0, %ebx
  movl $1, %eax
  int $0x80

.data
  msg:
    .ascii "Hello World\n"
    len = . - msg
